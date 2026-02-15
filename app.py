from fastapi import FastAPI, status, HTTPException
from schemas import RequestSchema
import feedparser


app = FastAPI()


data = {
    "a ": "https://habr.com/ru/rss/articles/",
    "a ": "https://google.com",
    "c": "https://habr.com/ru/rss/articles/",
}


def parse_articles(url: str, limit: int = 5):
    """Func to parce articles"""
    url = url.strip()
    feed = feedparser.parse(url)
    articles = []
    for article in feed["entries"][:limit]:
        articles.append({
            "title": article["title"],
            "link": article["link"],
        })
    return articles


@app.get("/sources")
def get_all_articles():
    return data

@app.get("/sources/articles")
def get_articles_from_all_resources(
        source_name: str | None = None,
        limit: int = 5,
        keyword: str | None = None
    ):
    if source_name not in data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found by name")
    
    info = parse_article_by_url(data[source_name])
    return {
        "name": source_name,
        "url": data[source_name],
        "information": info,
    }


@app.post("/sources/parse")
def parse_article_by_url(request: RequestSchema):
    """Parse, by url , return first 5 articles"""
    url = str(request.url).strip()
    data[request.name] = str(url)
    articles = parse_articles(url=url, limit=request.limit)
    return {
            "status": "saved",
            "source": request.name,
            "parsed" : articles,
        }


@app.post("/source")
def add_article(request: RequestSchema):
    """Simple adding article"""
    data[request.name] = str(request.url)
    return {"status":"saved"}



