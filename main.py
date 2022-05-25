# http://127.0.0.1:8000/docs # http://127.0.0.1:8000/redoc
from typing import Optional
from fastapi import FastAPI

app = FastAPI()  # uvicorn main:app --reload


# decorator /blog?limit=10&published=true
# (limit: int = 10, published: bool = True)
# only get 10 published blog posts

@app.get('/blog') ##using Optional helps not to recieve error if params are not provided
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


# to avoid conflicts between routes; this need to be above /blog/{id}
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit = 10):
    return {'data': {'comments': 'comment 1'}}
