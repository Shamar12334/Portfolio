from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, Contact as ContactSchema

router = APIRouter(
    prefix="/contact",
    tags =["Contact"]
)

#create contact
@router.post("/", response_model=ContactSchema)
def create_contact(contact: ContactCreate,db:Session=Depends(get_db)):
    new_contact= Contact(**contact.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact
#get contact
@router.get("/", response_model=list[ContactSchema])
def get_contact(db: Session= Depends(get_db)):
    contact= db.query(Contact).all()
    return contact
#update
@router.put("/{contact_id}", response_model=ContactSchema)
def update_contact(contact_id: int,updated: ContactCreate, db: Session = Depends(get_db)):
    contacts = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contacts:
        raise HTTPException(status_code=404,detail="not found")
    for key,value in updated.dict().items():
        setattr(contacts,key,value)
    db.commit()
    db.refresh(contacts)
    return contacts
#delete
@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db:Session=Depends(get_db)):
    contacts= db.query(Contact).filter(Contact.id == contact_id).first()
    if not contacts:
        raise HTTPException(status_code=404,detail="not found")
    db.delete(contacts)
    db.commit()
    return  {"message": "Project deleted successfully"}