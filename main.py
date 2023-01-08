from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blogs/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blogs/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blogs/{id}/comments')
def comments(id):
    return {'data': 'comments'}
