from pydantic import BaseModel



class Blog(BaseModel): # extend Blog with BaseModel
  title: str
  body: str