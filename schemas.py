from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    first_name: str
    last_name: str
    emp_id: str
    city: str
    age: int
    contact_no: int
    experience: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    emp_id: str

    class Config:
        orm_mode = True



