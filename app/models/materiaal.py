from sqlalchemy import Column, Integer, String, Float, Boolean

from app.database import Base


class Materiaal(Base):
    __tablename__ = "materialen"

    id = Column(Integer, primary_key=True, index=True)

    categorie = Column(String, nullable=False)

    merk = Column(String, nullable=True)

    artikelnummer = Column(String, nullable=True)

    omschrijving = Column(String, nullable=False)

    leverancier = Column(String, nullable=True)

    inkoopprijs = Column(Float, default=0)

    verkoopprijs = Column(Float, default=0)

    eenheid = Column(String, default="st")

    voorraad = Column(Integer, default=0)

    actief = Column(Boolean, default=True)