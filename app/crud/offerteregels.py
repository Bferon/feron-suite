from sqlalchemy.orm import Session

from app.models.offerte import Offerte
from app.models.offerteregel import OfferteRegel
from app.models.materiaal import Materiaal


def bereken_offerte_totaal(db: Session, offerte_id: int):

    offerte = (
        db.query(Offerte)
        .filter(Offerte.id == offerte_id)
        .first()
    )

    if not offerte:
        return

    subtotaal = sum(
        regel.totaal
        for regel in offerte.regels
    )

    btw = subtotaal * 0.21
    totaal = subtotaal + btw

    offerte.subtotaal = subtotaal
    offerte.btw = btw
    offerte.totaal = totaal

    db.commit()


def create_offerteregel(
    db: Session,
    offerte_id: int,
    materiaal_id: int,
    aantal: float = 1,
):

    materiaal = (
        db.query(Materiaal)
        .filter(Materiaal.id == materiaal_id)
        .first()
    )

    if not materiaal:
        return None

    regel = OfferteRegel(

        offerte_id=offerte_id,

        materiaal_id=materiaal.id,

        soort="Materiaal",

        omschrijving=materiaal.omschrijving,

        aantal=aantal,

        eenheid=materiaal.eenheid,

        prijs=materiaal.verkoopprijs,

        totaal=aantal * materiaal.verkoopprijs,

    )

    db.add(regel)
    db.commit()
    db.refresh(regel)

    bereken_offerte_totaal(
        db,
        offerte_id,
    )

    return regel


def create_arbeidregel(
    db: Session,
    offerte_id: int,
    omschrijving: str,
    uren: float,
    uurtarief: float,
):

    regel = OfferteRegel(

        offerte_id=offerte_id,

        materiaal_id=None,

        soort="Arbeid",

        omschrijving=omschrijving,

        aantal=uren,

        eenheid="uur",

        prijs=uurtarief,

        totaal=uren * uurtarief,

    )

    db.add(regel)
    db.commit()
    db.refresh(regel)

    bereken_offerte_totaal(
        db,
        offerte_id,
    )

    return regel


def create_tekstregel(
    db: Session,
    offerte_id: int,
    omschrijving: str,
):

    regel = OfferteRegel(

        offerte_id=offerte_id,

        materiaal_id=None,

        soort="Tekst",

        omschrijving=omschrijving,

        aantal=0,

        eenheid="",

        prijs=0,

        totaal=0,

    )

    db.add(regel)
    db.commit()
    db.refresh(regel)

    return regel


def get_offerteregel(
    db: Session,
    regel_id: int,
):

    return (
        db.query(OfferteRegel)
        .filter(OfferteRegel.id == regel_id)
        .first()
    )


def update_offerteregel(
    db: Session,
    regel_id: int,
    aantal: float,
):

    regel = get_offerteregel(
        db,
        regel_id,
    )

    if not regel:
        return None

    regel.aantal = aantal
    regel.totaal = aantal * regel.prijs

    db.commit()

    bereken_offerte_totaal(
        db,
        regel.offerte_id,
    )

    return regel


def delete_offerteregel(
    db: Session,
    regel_id: int,
):

    regel = get_offerteregel(
        db,
        regel_id,
    )

    if not regel:
        return

    offerte_id = regel.offerte_id

    db.delete(regel)
    db.commit()

    bereken_offerte_totaal(
        db,
        offerte_id,
    )