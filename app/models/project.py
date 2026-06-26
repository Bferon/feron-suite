from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class Project(Base):
    __tablename__ = "projecten"

    id = Column(Integer, primary_key=True, index=True)

    klant_id = Column(Integer, ForeignKey("klanten.id"))

    naam = Column(String)

    type = Column(String)

    status = Column(String)