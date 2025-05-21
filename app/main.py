import os
from flask import Flask, render_template, request
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

app = Flask(__name__)

# Load model and tokenizer once at startup
MODEL_NAME = "Pulk17/Fake-News-Detection"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["textInput"]
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()
    # Updated label mapping based on model config
    label_map = {0: "Real News", 1: "Fake News"}  # Swap if needed
    label = label_map[prediction]
    return render_template("index.html", prediction=label)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)