from fastapi import FastAPI
from typing import Optional

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
def comments(id):
    return {'data': 'comments'}
