# tests/test_items.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db import Base
from app import crud, schemas


def get_test_db():
    engine = create_engine("sqlite:///:memory:", future=True)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_create_and_list_items():
    db_gen = get_test_db()
    db = next(db_gen)

    item_in = schemas.ItemCreate(title="Test", description="Testing")
    item = crud.create_item(db, item_in)
    assert item.id is not None
    assert item.title == "Test"

    items = crud.list_items(db)
    assert len(items) == 1
    assert items[0].title == "Test"
