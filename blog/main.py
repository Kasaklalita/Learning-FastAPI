from fastapi import FastAPI
from . import models, schemas
from .database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()


@app.post('/blogs')
def create(blog: schemas.Blog):
    return {'title': blog.title, 'body': blog.body}
