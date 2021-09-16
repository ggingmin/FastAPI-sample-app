import uvicorn
import os

from app import app
from db import db
from models import Pizza as ModelPizza
from schema import Pizza as SchemaPizza

# app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post("/pizza/")
async def create_pizza(pizza: SchemaPizza):
    pizza_id = await ModelPizza.create(**pizza.dict())
    return {"pizza_id": pizza_id}

@app.get("/pizza/{id}", response_model=SchemaPizza)
async def get_pizza(id: int):
    pizza = await ModelPizza.get(id)
    return SchemaPizza(**pizza).dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)