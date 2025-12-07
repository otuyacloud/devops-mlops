# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas


def create_item(db: Session, item_in: schemas.ItemCreate) -> models.Item:
    item = models.Item(title=item_in.title, description=item_in.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def list_items(db: Session) -> list[models.Item]:
    return db.query(models.Item).order_by(models.Item.id).all()
