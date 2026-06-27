from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database import Base


class EssWizard(Base):
    __tablename__ = "ess_wizard"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(
        Integer,
        ForeignKey("projecten.id"),
        nullable=False,
    )

    # Netaansluiting
    netaansluiting = Column(String)
    hoofdzekering = Column(Integer)

    # Zonnepanelen
    pv_merk = Column(String)
    pv_omvormer = Column(String)
    aantal_panelen = Column(Integer)
    pv_vermogen_wp = Column(Integer)

    # Energie
    jaarverbruik = Column(Float, default=0)
    teruglevering = Column(Float, default=0)

    # Verbruikers
    elektrische_auto = Column(Boolean, default=False)
    warmtepomp = Column(Boolean, default=False)
    airco = Column(Boolean, default=False)
    koken_elektrisch = Column(Boolean, default=False)
    boiler = Column(Boolean, default=False)

    # Wensen
    noodstroom = Column(Boolean, default=False)
    dynamisch_contract = Column(Boolean, default=False)
    geen_teruglevering = Column(Boolean, default=False)
    volledig_zelfvoorzienend = Column(Boolean, default=False)

    # Advies
    batterij_capaciteit = Column(Float)
    geadviseerde_multiplus = Column(String)
    geadviseerde_accu = Column(String)
    geadviseerd_vermogen = Column(Float)

    # Victron componenten
    cerbo = Column(String)
    gx_touch = Column(String)
    energiemeter = Column(String)
    lynx = Column(String)

    # Notities
    opmerkingen = Column(String)

    project = relationship(
        "Project",
        backref="ess",
    )