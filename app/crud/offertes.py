from datetime import date, datetime

from sqlalchemy.orm import Session

from app.models.offerte import Offerte


OFFERTE_PREFIX = "OFF"


def generate_offertenummer(db: Session) -> str:
    """
    Genereert een offertenummer in de vorm:

    OFF-2026-0001
    """

    jaar = datetime.now().year

    prefix = f"{OFFERTE_PREFIX}-{jaar}-"

    offertes = (
        db.query(Offerte)
        .filter(Offerte.offertenummer.like(f"{prefix}%"))
        .all()
    )

    hoogste_nummer = 0

    for offerte in offertes:

        if not offerte.offertenummer:
            continue

        try:
            nummer = int(offerte.offertenummer.split("-")[-1])

            if nummer > hoogste_nummer:
                hoogste_nummer = nummer

        except ValueError:
            continue

    return f"{OFFERTE_PREFIX}-{jaar}-{hoogste_nummer + 1:04d}"


def create_offerte(db: Session, data: dict):

    data["offertenummer"] = generate_offertenummer(db)

    if "datum" not in data:
        data["datum"] = date.today()

    offerte = Offerte(**data)

    db.add(offerte)
    db.commit()
    db.refresh(offerte)

    return offerte


def get_offerte(db: Session, offerte_id: int):

    return (
        db.query(Offerte)
        .filter(Offerte.id == offerte_id)
        .first()
    )


def get_alle_offertes(db: Session):

    return (
        db.query(Offerte)
        .filter(Offerte.actief == True)
        .order_by(Offerte.id.desc())
        .all()
    )


def get_offertes_van_project(db: Session, project_id: int):

    return (
        db.query(Offerte)
        .filter(
            Offerte.project_id == project_id,
            Offerte.actief == True,
        )
        .order_by(Offerte.id.desc())
        .all()
    )


def update_offerte(db: Session, offerte_id: int, data: dict):

    offerte = get_offerte(db, offerte_id)

    if not offerte:
        return None

    for key, value in data.items():
        setattr(offerte, key, value)

    db.commit()
    db.refresh(offerte)

    return offerte


def verzend_offerte(
    db: Session,
    offerte_id: int,
):

    offerte = get_offerte(
        db,
        offerte_id,
    )

    if not offerte:
        return None

    offerte.status = "Verzonden"

    db.commit()
    db.refresh(offerte)

    return offerte


def accepteer_offerte(
    db: Session,
    offerte_id: int,
):

    offerte = get_offerte(
        db,
        offerte_id,
    )

    if not offerte:
        return None

    offerte.status = "Geaccepteerd"

    db.commit()
    db.refresh(offerte)

    return offerte


def wijs_offerte_af(
    db: Session,
    offerte_id: int,
):

    offerte = get_offerte(
        db,
        offerte_id,
    )

    if not offerte:
        return None

    offerte.status = "Afgewezen"

    db.commit()
    db.refresh(offerte)

    return offerte


def archive_offerte(db: Session, offerte_id: int):

    offerte = get_offerte(db, offerte_id)

    if not offerte:
        return None

    offerte.actief = False

    db.commit()

    return offerte


def restore_offerte(db: Session, offerte_id: int):

    offerte = get_offerte(db, offerte_id)

    if not offerte:
        return None

    offerte.actief = True

    db.commit()

    return offerte