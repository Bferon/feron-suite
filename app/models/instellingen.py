from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Instellingen(Base):
    __tablename__ = "instellingen"

    id = Column(Integer, primary_key=True, index=True)

    bedrijfsnaam = Column(String, default="Installatiebedrijf Feron")
    adres = Column(String, default="")
    postcode = Column(String, default="")
    plaats = Column(String, default="")
    telefoon = Column(String, default="")
    email = Column(String, default="")
    kvk = Column(String, default="")
    btw_nummer = Column(String, default="")

    uurtarief = Column(Float, default=62.50)
    voorrijkosten = Column(Float, default=35.00)
    btw_percentage = Column(Float, default=21.00)
    winstmarge = Column(Float, default=35.00)

    standaard_leverancier = Column(String, default="")