from sqlalchemy import Boolean, ForeignKey

# Column 是用來件資料行的Integer, String則是用來定義資料行的資料型態
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

# SQLAlchemy 的models是指 與數據庫交互的Class和instances。
# Pydantic   的models是指 數據驗證、轉換以及文檔的Class和instances。


# make the class of table => users(*id,email,hashed_password,is_active,Item)
class User(Base):
    # __tablename__可以幫助SQLAlchemy確認要存取哪個table
    __tablename__ = "users"

    # 建資料行
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # 建關係，back_populates是用來讓關係變成雙向的
    items = relationship("Item", back_populates="owner")


# make the class of table => users(*id,title,description,owner_id,owner)
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
