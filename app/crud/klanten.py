from sqlalchemy.orm import Session
from app.models.klant import Klant


def create_klant(db: Session, data: dict):
    klant = Klant(**data)
    db.add(klant)
    db.commit()
    db.refresh(klant)
    return klant