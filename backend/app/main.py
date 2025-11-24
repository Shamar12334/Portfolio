
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
app.include_router(status.router)

@app.get("/")
def read_root():
    return {"Hello": "fastapi backend running!"}
