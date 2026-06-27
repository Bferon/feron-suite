from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Project(Base):
    __tablename__ = "projecten"

    id = Column(Integer, primary_key=True, index=True)

    klant_id = Column(Integer, ForeignKey("klanten.id"), nullable=False)

    naam = Column(String, nullable=False)

    type = Column(String, nullable=False)

    status = Column(String, default="Nieuw")

    klant = relationship("Klant", backref="projecten")