from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# the URL of database
database_URL = "sqlite:///./FastAPI/sql_app.db"

# 預設情況 SQLite 只允許 one thread 以防止意外地對於不同的請求共享相同的連接。
# 但FastAPI可以用(def) 來多 theard訪問 

# engine 是用來執行SQL並回應解答的東西
engine = create_engine(database_URL, connect_args={"check_same_thread": False})

# Session 是 SQLite 中管理資料庫連接的一個概念，可以方便地管理資料庫操作和實現事務處理。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 用來定義一個Class是一種ORM Class 
Base = declarative_base()
