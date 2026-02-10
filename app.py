from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl
import feedparser

app = FastAPI()

data = {
    "a": "https://habr.com/ru/rss/articles/",
    "b": "https://habr.com/ru/rss/articles/",
    "c": "https://habr.com/ru/rss/articles/",
}



class Model(BaseModel):
    name: str
    url: HttpUrl

@app.get("/sources")
def get_all_article():
    """Получить все статьи"""
    return data

@app.post("/sources/parse")
def parse_article_by_url(request: Model):
    """Парсим, по url выводим первые 3 статьи"""
    feed = feedparser.parse(str(request.url))
    articles = []
    for article in feed["entries"]:
        articles.append({
            "title": article["title"],
            "link": article["link"],
        })    
    return articles[:3]
    

@app.post("/sources")
def add_url_to_db(request: Model):
    data[request.name] = str(request.url)
    return {"status": "saved"}
    
