from sqlalchemy.orm import Session

from app.models.instellingen import Instellingen


def get_instellingen(db: Session):
    """
    Haal de instellingen op.
    Bestaan ze nog niet, dan worden ze automatisch aangemaakt.
    """

    instellingen = db.query(Instellingen).first()

    if instellingen is None:

        instellingen = Instellingen()

        db.add(instellingen)
        db.commit()
        db.refresh(instellingen)

    return instellingen


def update_instellingen(db: Session, data: dict):
    """
    Werk de instellingen bij.
    """

    instellingen = get_instellingen(db)

    for key, value in data.items():
        setattr(instellingen, key, value)

    db.commit()
    db.refresh(instellingen)

    return instellingen