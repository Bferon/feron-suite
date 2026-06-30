from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    Boolean,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database import Base


class Factuur(Base):
    __tablename__ = "facturen"

    id = Column(Integer, primary_key=True, index=True)

    klant_id = Column(
        Integer,
        ForeignKey("klanten.id"),
        nullable=False,
    )

    project_id = Column(
        Integer,
        ForeignKey("projecten.id"),
        nullable=True,
    )

    offerte_id = Column(
        Integer,
        ForeignKey("offertes.id"),
        nullable=True,
    )

    factuurnummer = Column(
        String,
        unique=True,
        nullable=False,
    )

    datum = Column(Date)

    vervaldatum = Column(Date)

    status = Column(
        String,
        default="Concept",
    )

    subtotaal = Column(
        Float,
        default=0,
    )

    btw = Column(
        Float,
        default=0,
    )

    totaal = Column(
        Float,
        default=0,
    )

    betaald = Column(
        Boolean,
        default=False,
    )

    opmerkingen = Column(String)

    actief = Column(
        Boolean,
        default=True,
    )

    klant = relationship(
        "Klant",
    )

    project = relationship(
        "Project",
    )

    offerte = relationship(
        "Offerte",
    )

    regels = relationship(
        "FactuurRegel",
        back_populates="factuur",
        cascade="all, delete-orphan",
    )