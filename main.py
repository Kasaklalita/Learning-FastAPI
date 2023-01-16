from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Veniamin'}}


@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blogs/{id}')
def show(id: int):
    return {'data': id}


@app.get('blogs/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}
