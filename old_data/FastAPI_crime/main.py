from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

tags_metadata = [{"name": "Get"}, {"name": "Post"}, {"name": "Put"}, {"name": "Delete"}]
app = FastAPI(openapi_tags=tags_metadata)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/crime/", tags=["Get"], response_model=list[schemas.Crime])
def read_crimes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_crimes(db, skip=skip, limit=limit)
    return users


@app.get("/crime/{crime_id}", tags=["Get"], response_model=schemas.Crime)
def read_crime(crime_id: int, db: Session = Depends(get_db)):
    db_crime = crud.get_crime_by_id(db, crime_id=crime_id)
    if db_crime is None:
        raise HTTPException(status_code=404, detail="crime not found")
    return db_crime

@app.post("/crime/", tags=["Post"], response_model=schemas.Crime)
def create_crime(crime: schemas.CrimeCreate, db: Session = Depends(get_db)):
    # db_user = crud.get_crime(db, crime_id=user.oc_dt)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.post_crime(db=db, Crime=crime)


@app.put("/crime/{crime_id}", tags=["Get"], response_model=schemas.Crime)
def update_crime(crime_id: int,crime: schemas.CrimeCreate, db: Session = Depends(get_db)):
    # db_crime = crud.get_crime_by_id(db, crime_id=crime_id)
    # if db_crime is None:
    #     raise HTTPException(status_code=404, detail="crime not found")
    # else:
        crud.put_crime(db, Crime=crime,Crime_id=crime_id)

