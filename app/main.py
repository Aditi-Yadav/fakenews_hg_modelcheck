import os
from flask import Flask, render_template, request
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from PIL import Image
import pytesseract

app = Flask(__name__)

MODEL_NAME = "Pulk17/Fake-News-Detection"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", prediction=None, extracted_text=None)

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("textInput", "")
    extracted_text = None

    # Check if an image was uploaded
    if "imageInput" in request.files:
        image_file = request.files["imageInput"]
        if image_file and image_file.filename != "":
            image = Image.open(image_file.stream)
            extracted_text = pytesseract.image_to_string(image)
            text = extracted_text  # Use extracted text for prediction

    if not text.strip():
        return render_template("index.html", prediction="No text provided.", extracted_text=extracted_text)

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()
    label_map = {0: "Real News", 1: "Fake News"}
    label = label_map[prediction]
    return render_template("index.html", prediction=label, extracted_text=extracted_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)