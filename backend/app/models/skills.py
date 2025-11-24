from sqlalchemy import Column,String,Text,Integer
from app.core.database import Base

class Skill(Base):
    __tablename__= "skills"

    id = Column(Integer, primary_key=True,index=True)
    skill_name= Column(String(200),nullable=False)
    category= Column(String(200),nullable=False)