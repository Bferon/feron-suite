from sqlalchemy.orm import Session

from app.models.materiaal import Materiaal


def get_materialen(db: Session):
    return (
        db.query(Materiaal)
        .filter(Materiaal.actief == True)
        .order_by(
            Materiaal.categorie,
            Materiaal.merk,
            Materiaal.omschrijving,
        )
        .all()
    )


def get_gearchiveerde_materialen(db: Session):
    return (
        db.query(Materiaal)
        .filter(Materiaal.actief == False)
        .order_by(
            Materiaal.categorie,
            Materiaal.merk,
            Materiaal.omschrijving,
        )
        .all()
    )


def get_materiaal(db: Session, materiaal_id: int):
    return (
        db.query(Materiaal)
        .filter(Materiaal.id == materiaal_id)
        .first()
    )


def create_materiaal(db: Session, data: dict):

    materiaal = Materiaal(**data)

    db.add(materiaal)
    db.commit()
    db.refresh(materiaal)

    return materiaal


def update_materiaal(db: Session, materiaal_id: int, data: dict):

    materiaal = get_materiaal(db, materiaal_id)

    if not materiaal:
        return None

    for key, value in data.items():
        setattr(materiaal, key, value)

    db.commit()
    db.refresh(materiaal)

    return materiaal


def archive_materiaal(db: Session, materiaal_id: int):

    materiaal = get_materiaal(db, materiaal_id)

    if not materiaal:
        return None

    materiaal.actief = False

    db.commit()

    return materiaal


def restore_materiaal(db: Session, materiaal_id: int):

    materiaal = get_materiaal(db, materiaal_id)

    if not materiaal:
        return None

    materiaal.actief = True

    db.commit()

    return materiaal