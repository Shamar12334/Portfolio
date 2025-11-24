from pydantic import BaseModel
from datetime import datetime

class ContactBase(BaseModel):
    name: str
    email: str 
    message : str
    time_stamp: datetime
class ContactCreate(ContactBase):
    pass 
class Contact(ContactBase):
    id:int

    class Config:
        from_attributes=True