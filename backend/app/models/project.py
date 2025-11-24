from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    github_url = Column(String(300), nullable=True)
    live_url = Column(String(300), nullable=True)
    tech_stack = Column(String(300), nullable=True)
    image_url = Column(String(300), nullable=True)
