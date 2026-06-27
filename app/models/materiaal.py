from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
)

from app.database import Base


class Materiaal(Base):
    __tablename__ = "materialen"

    id = Column(Integer, primary_key=True, index=True)

    # Algemene gegevens
    categorie = Column(String, nullable=False)
    omschrijving = Column(String, nullable=False)
    merk = Column(String)
    fabrikant = Column(String)
    artikelnummer = Column(String)
    leverancier = Column(String)

    # ESS
    ess_component = Column(Boolean, default=False)
    component_type = Column(String)

    # Technische gegevens
    datasheet = Column(String)
    afbeelding = Column(String)

    # Prijzen
    inkoopprijs = Column(Float, default=0)
    verkoopprijs = Column(Float, default=0)

    # Voorraad
    eenheid = Column(String, default="st")
    voorraad = Column(Integer, default=0)

    # Status
    actief = Column(Boolean, default=True)