from sqlalchemy.orm import Session

from . import models, schemas


# get part
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


# post part
def post_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def post_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def put_item(db: Session, item_id: int, item_title: str, item_description: str):
    if db.query(models.Item).filter(models.Item.id == item_id).first() == None:
        return None
    else:
        p = db.query(models.Item).filter(models.Item.id == item_id).first()
        p.title = item_title
        p.description = item_description
        db.commit()
        return p


def put_user(db: Session, user_id: int, user_email: str, user_active: bool):
    if db.query(models.User).filter(models.User.id == user_id).first() == None:
        return None
    else:
        p = db.query(models.User).filter(models.User.id == user_id).first()
        p.email = user_email
        p.is_active = user_active
        db.commit()
        return {"message": "user update successfully"}


def delete_item(db: Session, item_id: int):
    if db.query(models.Item).filter(models.Item.id == item_id).first() == None:
        return None
    else:
        db.query(models.Item).filter(models.Item.id == item_id).delete()
        db.commit()
        return {"message": "Item deleted successfully"}


def delete_user(db: Session, user_id: int):
    if db.query(models.User).filter(models.User.id == user_id).first() == None:
        return None
    else:
        db.query(models.Item).filter(models.Item.owner_id == user_id).delete()
        db.query(models.User).filter(models.User.id == user_id).delete()
        db.commit()
        return {"message": "user and its Item deleted successfully"}
