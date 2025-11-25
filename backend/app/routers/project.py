from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, Project as ProjectSchema

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)
# create a project
@router.post("/", response_model=ProjectSchema)
def create_project(project: ProjectCreate,db: Session= Depends(get_db)):
    new_project = Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
#get all projects
@router.get("/", response_model=list[ProjectSchema])
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
# get one project by ID
@router.get("/{project_id}",response_model=ProjectSchema)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404,detail="Project not found")
    return project
# UPDATE PROJECT
@router.put("/{project_id}", response_model=ProjectSchema)
def update_project(project_id: int, updated: ProjectCreate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    for key, value in updated.dict().items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)
    return project
# DELETE PROJECT
@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}
