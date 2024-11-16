from fastapi import FastAPI, Query, Header, Response
from typing import Annotated, Union
from pydantic import BaseModel
import asyncio

app = FastAPI()

items = ["T-Shirt", "Shirt", "Pants", "Shoes"]

@app.get("/")
def read_root():
    return {"message" : "Hello Osouzai"}

@app.get("/items/{item_id}")
def read_item(item_id: str, skip: int, limit: Annotated[int,Query(ge=1, le=10)] = 10):
    return {"items": items[skip : skip + limit] }

@app.get("/items/item")
def read_items(skip: int = 0, limit: Annotated[int, Query(gt=0, le=10)] = 10): 
    return {"items": items[skip : skip + limit]}

class Item(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None

@app.post("/items")
def create_item(item: Item):
    print(f"データを登録します: {item.name}, {item.price}, {item.description }")
    return item

@app.get("/sample/")
def read_sample(
    response: Response, 
    authorization: Union[str, None] = Header(default= None)):
    print(authorization)
    response.headers["custom-header"] = "12345"
    return{"messaga" : "ヘッダー情報を登録しました"}

@app.get("/sleep_time/")
async def sleep_time(sec : int):
    await asyncio.sleep(sec)

if __name__ == "__main__":
    asyncio.run(main())
