
from fastapi import FastAPI
from app.routers import status
import app.models
from app.core.database import Base,engine

app = FastAPI(
    title="Portfolio API",
    version= "1.0.0",
    description="backend API for my personal portfolio"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

from app.routers import(
    status_router,
    project_router,
    about_router,
    skills_router,
    contact_router
)
app.include_router(status.router)
app.include_router(project_router)
app.include_router(about_router)
app.include_router(skills_router)
app.include_router(contact_router)

@app.get("/")
def read_root():
    return {"Hello": "fastapi backend running!"}
