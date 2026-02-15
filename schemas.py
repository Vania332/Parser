from pydantic import BaseModel, HttpUrl


class RequestSchema(BaseModel):
    name: str
    url: HttpUrl
    limit: int = 5 