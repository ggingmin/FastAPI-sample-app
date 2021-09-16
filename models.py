import sqlalchemy
from db import db, metadata, sqlalchemy

pizzas = sqlalchemy.Table(
    "pizzas",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Integer),
    sqlalchemy.Column("is_cheese_stuffed", sqlalchemy.Boolean, default=False, server_default='False')
)


class Pizza:
    @classmethod
    async def get(cls, id):
        query = pizzas.select().where(pizzas.c.id == id)
        pizza = await db.fetch_one(query)
        return pizza
    
    @classmethod
    async def create(cls, **pizza):
        query = pizzas.insert().values(**pizza)
        pizza_id = await db.execute(query)
        return pizza_id