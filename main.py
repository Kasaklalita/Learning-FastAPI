from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blogs')
def index(limit=10, published=True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blogs/{id}')
def show(id: int):
    return {'data': id}


@app.get('blogs/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blogs')
def create_blog(blog: Blog):
    return blog
    return {'data': 'blog is created'}
