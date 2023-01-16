from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str


@app.post('/blogs')
def create(blog: Blog):
    return {'title': blog.title, 'body': blog.body}
