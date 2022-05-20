from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
  return {'data': {'name': 'John Doe'}}


@app.get('/about')
def about():
  return {'data': {'page': 'About'}}
