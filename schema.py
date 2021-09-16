from pydantic import BaseModel

class Pizza(BaseModel):

    name: str
    price: int
    is_cheese_stuffed: bool

    class Config:
        orm_mode = True