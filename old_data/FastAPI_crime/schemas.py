# 因為 SQLAlchemy 跟 Pydantic 對model的定義不一樣，所以 Pydantic 的 model 一律以 schemas 來對待
from pydantic import BaseModel

# 小tip
# SQLAlchemy的寫法是 name = Column(String)
# Pydantic  的寫法是 name: str

# 用 Pydantic 的 model 來創建創建 ItemBase 和 UserBase。
class CrimeBase(BaseModel):
    oc_dt: str
    oc_p1: str

# 最後創建一個回傳用的 class 來確保 id 之類自動產生的欄目，會跟著傳回去
class Crime(CrimeBase):
    id: int

    class Config:
        orm_mode = True

class CrimeCreate(CrimeBase):
    pass