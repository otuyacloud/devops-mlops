# app/main.py
from flask import Flask, jsonify, request
from sqlalchemy.orm import Session

from .config import Config
from .db import Base, engine, get_db
from . import crud, schemas


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Create tables (for demo; in real prod you'd run migrations)
    Base.metadata.create_all(bind=engine)

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok", "environment": Config.ENVIRONMENT})

    @app.route("/items", methods=["GET"])
    def list_items():
        db_gen = get_db()
        db: Session = next(db_gen)
        try:
            items = crud.list_items(db)
            return jsonify(
                [
                    {
                        "id": item.id,
                        "title": item.title,
                        "description": item.description,
                    }
                    for item in items
                ]
            )
        finally:
            try:
                next(db_gen)
            except StopIteration:
                pass

    @app.route("/items", methods=["POST"])
    def create_item():
        payload = request.get_json(force=True, silent=True) or {}
        title = payload.get("title")
        description = payload.get("description")

        if not title:
            return jsonify({"message": "title is required"}), 400

        item_in = schemas.ItemCreate(title=title, description=description)

        db_gen = get_db()
        db: Session = next(db_gen)
        try:
            item = crud.create_item(db, item_in)
            return (
                jsonify(
                    {
                        "id": item.id,
                        "title": item.title,
                        "description": item.description,
                    }
                ),
                201,
            )
        finally:
            try:
                next(db_gen)
            except StopIteration:
                pass

    return app


# For local debug (not used in Docker CMD)
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
