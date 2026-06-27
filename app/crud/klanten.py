from sqlalchemy.orm import Session
from app.models.klant import Klant


def create_klant(db: Session, data: dict):
    klant = Klant(**data)
    db.add(klant)
    db.commit()
    db.refresh(klant)
    return klant


def get_klant(db: Session, klant_id: int):
    return db.query(Klant).filter(Klant.id == klant_id).first()


def update_klant(db: Session, klant_id: int, data: dict):
    klant = get_klant(db, klant_id)

    if not klant:
        return None

    for key, value in data.items():
        setattr(klant, key, value)

    db.commit()
    db.refresh(klant)

    return klant