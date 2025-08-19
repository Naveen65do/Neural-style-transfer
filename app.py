from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import torch
from transformer_net import TransformerNet
import utils
from torchvision import transforms
import re

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load style models into a dictionary (add your trained models here)
STYLE_MODELS = {
    "Mosaic": "models/mosaic.pth",
    "rain_princess": "models/rain_princess.pth",
    "udnie":"models/udnie.pth",
    "Candy": "models/candy.pth"
}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model(path):
    style_model = TransformerNet()
    state_dict = torch.load(path, map_location=device)
    for k in list(state_dict.keys()):
        if re.search(r'in\d+\.running_(mean|var)$', k):
            del state_dict[k]
    style_model.load_state_dict(state_dict)
    style_model.to(device).eval()
    return style_model

@app.route("/")
def index():
    return render_template("index.html", styles=STYLE_MODELS.keys())

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        style = request.form.get("style")
        file = request.files["content_image"]

        if file and style in STYLE_MODELS:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Load model for selected style
            model = load_model(STYLE_MODELS[style])

            # Preprocess image
            image = utils.load_image(filepath)
            transform = transforms.Compose([
                transforms.ToTensor(),
                transforms.Lambda(lambda x: x.mul(255))
            ])
            image = transform(image).unsqueeze(0).to(device)

            # Stylize
            with torch.no_grad():
                output = model(image).cpu()

            output_path = os.path.join(OUTPUT_FOLDER, "styled_" + file.filename)
            utils.save_image(output_path, output[0])

            return redirect(url_for("result", filename="styled_" + file.filename))

    return render_template("upload.html", styles=STYLE_MODELS.keys())

@app.route("/gallery")
def gallery():
    files = os.listdir(OUTPUT_FOLDER)
    # Only show image files
    images = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    return render_template("gallery.html", images=images)


@app.route("/result/<filename>")
def result(filename):
    return render_template("result.html", filename=filename)

@app.route("/outputs/<filename>")
def send_output(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
