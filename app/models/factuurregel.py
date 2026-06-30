from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database import Base


class FactuurRegel(Base):
    __tablename__ = "factuur_regels"

    id = Column(Integer, primary_key=True, index=True)

    factuur_id = Column(
        Integer,
        ForeignKey("facturen.id"),
        nullable=False,
    )

    volgorde = Column(
        Integer,
        default=1,
    )

    soort = Column(
        String,
        default="Materiaal",
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

    totaal = Column(
        Float,
        default=0,
    )

    factuur = relationship(
        "Factuur",
        back_populates="regels",
    )