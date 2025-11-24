from pydantic import BaseModel
class ProjectBase(BaseModel):
    title: str
    description: str
    github_url: str | None = None
    live_url: str | None = None
    tech_stack: str | None= None
    image_url: str | None = None

class ProjectCreate(ProjectBase):
     pass
class Project(ProjectBase):
    id : int

    class Config:
        from_attributes=True