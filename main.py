from fastapi import FastAPI    # http://127.0.0.1:8000/docs # http://127.0.0.1:8000/redoc

app = FastAPI() #uvicorn main:app --reload


@app.get('/') ##decorator
def index():
  return {'data': 'home page'}


@app.get('/blog/unpublished') ## to avoid conflicts between routes; this need to be above /blog/{id}
def unpublished():
  return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
  # fetch blog with id = id
  return {'data': id}


@app.get('/blog/{id}/comments')
def comments():
  return {'data': {'comments': 'comment 1'}}