from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.skills import Skill
from app.schemas.skills import SkillCreate, Skill as SkillSchema

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)

#create skills
@router.post("/", response_model=SkillSchema)
def create_skills(skills: SkillCreate, db: Session = Depends(get_db)):
    new_skills= Skill(**skills.dict())
    db.add(new_skills)
    db.commit()
    db.refresh(new_skills)
    return new_skills
# get all skills
@router.get("/", response_model=list[SkillSchema])
def get_skills(db: Session= Depends(get_db)):
    skills= db.query(Skill).all()
    if not skills:
        raise HTTPException(status_code=404,detail="skills not found")
    return skills
#update
@router.put("/{skill_id}",response_model=SkillSchema)
def update_skills(skill_id: int,updated:SkillCreate, db: Session=Depends(get_db)):
    skill= db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404,detail="not found")
    for key, value in updated.dict().items():
        setattr(skill,key,value)
    db.commit()
    db.refresh(skill)
    return skill
#delete
@router.delete("/{skill_id}")
def delete_skills(skill_id : int,db:Session=Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404,detail="not found")
    db.delete(skill)
    db.commit()
    return {"message":"successfully deleted"}