from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": "Get"},
    {"name": "Post"},
    {"name": "Put"},
    {"name": "Delete"}
]
app = FastAPI(openapi_tags=tags_metadata)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", tags=["Get"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", tags=["Get"], response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    print("db_user == " + str(db_user))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/items/", tags=["Get"], response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/users/", tags=["Post"], response_model=schemas.User)
def post_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.post_user(db=db, user=user)


@app.post("/users/items/{user_id}", tags=["Post"], response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.post_item(db=db, item=item, user_id=user_id)


@app.put("/items/{item_id}", tags=["Put"], response_model=schemas.Item)
def update_item(item_id: int, item_title: str, item_description: str, db: Session = Depends(get_db)):
    ans = crud.put_item(db, item_id,item_title,item_description)
    if ans == None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return ans
    
@app.put("/user/{user_id}", tags=["Put"])
def update_user(user_id: int, user_email: str, user_active: bool, db: Session = Depends(get_db)):
    ans = crud.put_user(db, user_id,user_email,user_active)
    if ans == None:
        raise HTTPException(status_code=404, detail="user not found")
    else:
        return ans
    
@app.delete("/items/{item_id}", tags=["Delete"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    ans = crud.delete_item(db, item_id)
    if ans == None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return ans


@app.delete("/user/{user_id}", tags=["Delete"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    ans = crud.delete_user(db, user_id)
    if ans == None:
        raise HTTPException(status_code=404, detail="user not found")
    else:
        return ans
