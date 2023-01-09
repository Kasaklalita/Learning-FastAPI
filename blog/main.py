from fastapi import FastAPI
from . import schemas


app = FastAPI()


@app.post('/blogs')
def create(request: schemas.Blog):
    return request
