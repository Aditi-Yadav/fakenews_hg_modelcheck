from transformers import pipeline

class FakeNewsDetector:
    def __init__(self):
        self.model = pipeline("text-classification", model="jy46604790/Fake-News-Bert-Detect")

    def predict(self, text):
        result = self.model(text)
        return result[0]['label'], result[0]['score']