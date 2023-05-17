from sqlalchemy.orm import Session

from . import models, schemas


# get part
def get_crime_by_id(db: Session, crime_id: int):
    return db.query(models.Crime).filter(models.Crime.id == crime_id).first()

def get_crimes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Crime).offset(skip).limit(limit).all()

# post part "1110401""臺南市新營區"
def post_crime(db: Session, Crime: schemas.CrimeCreate):
    db_crime = models.Crime(oc_dt=Crime.oc_dt, oc_p1=Crime.oc_p1)
    db.add(db_crime)
    db.commit()
    db.refresh(db_crime)
    return db_crime


def put_crime(db: Session, Crime: schemas.CrimeCreate,Crime_id: int):
    if db.query(models.Crime).filter(models.Crime.id == Crime_id).first() == None:
        return None
    else:
        p=db.query(models.Crime).filter(models.Crime.id == Crime_id).first()
        p.oc_dt = Crime.oc_dt
        p.oc_p1 = Crime.oc_p1
        db.commit()
        # return {"message": "Crime update successfully"}

def delete_user(db: Session, Crime_id: int):
    if db.query(models.Crime).filter(models.Crime.id == Crime_id).first() == None:
        return None
    else:
        db.query(models.Crime).filter(models.Crime.id == Crime_id).delete()
        db.commit()
        # return {"message": "user and its Item deleted successfully"}
