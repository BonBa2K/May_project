# 因為 SQLAlchemy 跟 Pydantic 對model的定義不一樣，所以 Pydantic 的 model 一律以 schemas 來對待
from pydantic import BaseModel

# 小tip
# SQLAlchemy的寫法是 name = Column(String)
# Pydantic  的寫法是 name: str


# 用 Pydantic 的 model 來創建創建 ItemBase 和 UserBase。
class ItemBase(BaseModel):
    title: str
    description: str | None = None


# 並創建一個 Create 來確保 User 的 password 在 GET 的時候不會被一併取得
class ItemCreate(ItemBase):
    pass


# 最後創建一個回傳用的 class 來確保 id 之類自動產生的欄目，會跟著傳回去
class Item(ItemBase):
    id: int
    owner_id: int

    # configurations to replace " id = data["id"] " to" id = data.id "
    class Config:
        orm_mode = True


# the User part
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
