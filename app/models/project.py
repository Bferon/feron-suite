from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    Date,
    Float,
    Text,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Project(Base):
    __tablename__ = "projecten"

    id = Column(Integer, primary_key=True, index=True)

    klant_id = Column(Integer, ForeignKey("klanten.id"), nullable=False)

    projectnummer = Column(String, unique=True, nullable=True)

    naam = Column(String, nullable=False)

    type = Column(String, nullable=False)

    status = Column(String, default="Nieuw")

    startdatum = Column(Date, nullable=True)

    einddatum = Column(Date, nullable=True)

    offertebedrag = Column(Float, default=0)

    opmerkingen = Column(Text)

    actief = Column(Boolean, default=True)

    klant = relationship("Klant", backref="projecten")