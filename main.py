from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blogs')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} blogs from the database'}


@app.get('/blogs/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blogs/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blogs/{id}/comments')
def comments(id, limit = 10):
    return limit


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blogs')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with {blog.title}'}