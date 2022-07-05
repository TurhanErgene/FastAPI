from fastapi import FastAPI, Depends, Response, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()

# whenever we find any model, create it in the database
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db  ##yield is a keyword that is used like return, except the function will return a generator.
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete("/blog{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=404, detail=f"Blog with the id: {id} has not found"
        )

    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog deleted"


@app.put("/blog{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id: {id} has not found",
        )
    blog.update(request.dict())  # {'title': request.title, 'body': request.body}
    db.commit()
    return "Blog updated"


@app.get("/blog/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog)
def one(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=404, detail=f"Blog with the id: {id} has not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with the id: {id} has not found"}
    return blog


@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    


