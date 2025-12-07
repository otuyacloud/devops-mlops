# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .db import Base, engine, get_db
from .config import settings
from . import crud, schemas, models

# Create tables on startup (for demo; in real prod you'd do migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok", "environment": settings.environment}


@app.get("/items", response_model=list[schemas.ItemRead], tags=["items"])
def list_items_endpoint(db: Session = Depends(get_db)):
    items = crud.list_items(db)
    return items


@app.post("/items", response_model=schemas.ItemRead, tags=["items"])
def create_item_endpoint(item_in: schemas.ItemCreate, db: Session = Depends(get_db)):
    item = crud.create_item(db, item_in)
    return item
