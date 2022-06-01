from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel): # extend Blog with BaseModel
  title: str
  body: str

@app.post('/blog')
def create(request: Blog):
    return request

