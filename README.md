# Neural-style-transfer

COMPANY: CODETECH IT SOLUTIONS

NAME: NAVEEN.R

INTERN ID:CT08DY717

DOMAIN NAME: ARTIFICIAL INTELLIGENCE

DURATION: 8 WEEKS

MENTOR: NEELA SANTHOSH

DESCRIPTION:

Project Description:

📌 Objective:

The goal of this project is to create a web-based application that allows users to upload a photo and apply different artistic styles (e.g., Mosaic, Candy, Udnie, Rain Princess) using pretrained neural style transfer models. The final output is a stylized version of the uploaded image which can be viewed and downloaded from a result page or gallery.

How It Works:

User Interface (Frontend):

The user visits the home page and selects an image file and a desired style.

The file is uploaded via an HTML form to the backend server.

Backend (Flask + PyTorch):

Upon image upload, Flask saves the image in a designated upload folder.

A corresponding style transfer model is loaded using PyTorch.

The uploaded image is preprocessed, passed through the model, and the output is saved.

The user is redirected to a result page displaying the styled image.

Image Gallery:

A gallery route displays all previously styled images from the outputs folder.

 Tools & Technologies Used
 Backend:

Python 3.x

Flask – Lightweight web framework for handling routes, uploads, and rendering templates.

PyTorch – Deep learning library used to load and run style transfer models.

Torchvision – For image transformations and preprocessing.

 Frontend:

HTML5

Jinja2 Templating – Used with Flask to dynamically render HTML content.

CSS (optional, for styling the UI – can be included separately)

Workflow:

Start Server:

python app.py


Navigate to Homepage:

http://127.0.0.1:5000/

Upload Image:

Select an image and a style.

Click upload.

Wait for server to process and return the stylized image.

View Results:

Stylized image shown on result page.

Option to view all results in gallery.

📦 Model Details:

Pretrained Fast Neural Style Transfer Models (like Johnson et al.’s feedforward network).

Models are loaded from .pth files in the models/ directory.

Each model applies a different style in a fraction of a second.

✅ Features:

Upload any JPEG/PNG image.

Choose from multiple artistic styles.

Fast image processing using PyTorch.

Output image preview and gallery view.

Device-aware (uses GPU if available).


OUTPUT:
<img width="1893" height="931" alt="image" src="https://github.com/user-attachments/assets/c06b67ab-3611-4aac-891f-8f79394a4b15" />
