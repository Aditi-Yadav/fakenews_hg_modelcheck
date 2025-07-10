from flask import Blueprint, render_template, request
from .model import predict_fake_news

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = predict_fake_news(text)
    return render_template('index.html', result=result)