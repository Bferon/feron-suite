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


class Offerte(Base):
    __tablename__ = "offertes"

    id = Column(Integer, primary_key=True, index=True)

    klant_id = Column(
        Integer,
        ForeignKey("klanten.id"),
        nullable=False,
    )

    project_id = Column(
        Integer,
        ForeignKey("projecten.id"),
        nullable=False,
    )

    offertenummer = Column(
        String,
        unique=True,
        nullable=False,
    )

    datum = Column(Date)

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

    opmerkingen = Column(String)

    actief = Column(
        Boolean,
        default=True,
    )

    klant = relationship(
        "Klant",
        backref="offertes",
    )

    project = relationship(
        "Project",
        backref="offertes",
    )