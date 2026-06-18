from fastapi import FastAPI
# from pydantic import BaseModel
from app.routes.issues import router as issues_router

# class Item(BaseModel):
# item_id: str
# value: str


app = FastAPI()


@app.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}


app.include_router(issues_router)

# items = [
#   Item(item_id="foo", value="The Foo Item"),
# Item(item_id="bar", value="The Bar Item"),
# Item(item_id="baz", value="The Baz Item"),
# ]


# @app.get("/health")
# def health_check():
# return {"status": "ok"}


# @app.get("/items")
# def get_items():
#   return items


# @app.get("/items/{item_id}")
# def get_item(item_id: str):
#   for item in items:
#      if item.item_id == item_id:
#        return item
# return {"error": "Item not found"}


# @app.post("/items")
# def create_item(item: Item):
#   items.append(item)
#  return item
