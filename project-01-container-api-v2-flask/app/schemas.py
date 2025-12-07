# app/schemas.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class ItemCreate:
    title: str
    description: Optional[str] = None
