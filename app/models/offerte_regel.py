from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database import Base


class OfferteRegel(Base):
    __tablename__ = "offerte_regels"

    id = Column(Integer, primary_key=True, index=True)

    offerte_id = Column(
        Integer,
        ForeignKey("offertes.id"),
        nullable=False,
    )

    materiaal_id = Column(
        Integer,
        ForeignKey("materialen.id"),
        nullable=True,
    )

    omschrijving = Column(
        String,
        nullable=False,
    )

    aantal = Column(
        Float,
        default=1,
    )

    eenheid = Column(
        String,
        default="st",
    )

    prijs = Column(
        Float,
        default=0,
    )

    korting = Column(
        Float,
        default=0,
    )

    totaal = Column(
        Float,
        default=0,
    )

    offerte = relationship("Offerte")

    materiaal = relationship("Materiaal")