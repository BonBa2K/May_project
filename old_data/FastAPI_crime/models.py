from sqlalchemy import Boolean, ForeignKey

# Column 是用來件資料行的Integer, String則是用來定義資料行的資料型態
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

# SQLAlchemy 的models是指 與數據庫交互的Class和instances。
# Pydantic   的models是指 數據驗證、轉換以及文檔的Class和instances。


# make the class of table => users(*id,email,hashed_password,is_active,Item)
class Crime(Base):
    # __tablename__可以幫助SQLAlchemy確認要存取哪個table
    __tablename__ = "crime"

    # 建資料行
    id = Column(Integer, primary_key=True, index=True)
    oc_dt = Column(String, index=True)
    oc_p1 = Column(String, index=True)

    # owner = relationship("User", back_populates="items")
