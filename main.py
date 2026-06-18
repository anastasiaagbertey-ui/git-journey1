from fastapi import FastAPI
# from pydantic import BaseModel
from app.routes.issues import router as issues_router
import uvicorn
import os

# class Item(BaseModel):
# item_id: str
# value: str


app = FastAPI()


@app.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}


app.include_router(issues_router, prefix="/api/v1/issues", tags=["issues"])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

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
