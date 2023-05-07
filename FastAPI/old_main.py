from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 建立資料庫
database = []

# 資料模型
class Item(BaseModel):
    name: str
    price: float

# 新增資料 API
@app.post("/items/")
async def create_item(item: Item):
    database.append(item.dict())
    return item

# 取得所有資料 API
@app.get("/items/")
async def read_items():
    return database

# 取得特定資料 API
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    try:
        return database[item_id]
    except:
        raise HTTPException(status_code=404, detail="Item not found")

# 更新特定資料 API
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    try:
        database[item_id] = item.dict()
        return {"message": "Item updated successfully"}
    except:
        raise HTTPException(status_code=404, detail="Item not found")

# 刪除特定資料 API
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    try:
        database.pop(item_id)
        return {"message": "Item deleted successfully"}
    except:
        raise HTTPException(status_code=404, detail="Item not found")
