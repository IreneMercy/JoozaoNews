from app import app
import urllib.request, json
from .models import news

News = news.News

api_key = '87082138d3fc4755892f9c7266f6ceea'
query = 'lipstick'
base_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(query,api_key)

def get_news_source():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(base_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results


def process_results(news_results_list):
    news_results= []
    for news_item in news_results_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt= news_item.get('publishedAt')
        content = news_item.get('content')

        if author:
            news_obj = News(id, name, author,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_obj)
    print(news_results)
    return news_results
