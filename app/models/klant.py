from sqlalchemy import Column, Integer, String

from app.database import Base


class Klant(Base):
    __tablename__ = "klanten"

    id = Column(Integer, primary_key=True, index=True)

    naam = Column(String, nullable=False)

    adres = Column(String)

    postcode = Column(String)

    plaats = Column(String)

    telefoon = Column(String)

    email = Column(String)