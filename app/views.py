from flask import render_template
from .request import get_news_source, process_results
from app import app

@app.route('/')
def index():
    results = get_news_source()
    return render_template('index.html', results = results)

@app.route('/news/<news_id>')
def news(news_id):
    return render_template('news.html', id = news_id)
