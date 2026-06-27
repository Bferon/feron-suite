from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
    Text,
)

from sqlalchemy.orm import relationship

from app.database import Base


class EssConfiguratie(Base):
    __tablename__ = "ess_configuraties"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(
        Integer,
        ForeignKey("projecten.id"),
        nullable=False,
        unique=True,
    )

    # Net
    netaansluiting = Column(String)
    dynamisch_contract = Column(Boolean, default=False)

    # Energie
    jaarverbruik = Column(Float, default=0)
    teruglevering = Column(Float, default=0)

    # PV
    pv_vermogen = Column(Float, default=0)
    pv_omvormer = Column(String)

    # Victron
    multiplus = Column(String)
    cerbo_gx = Column(Boolean, default=False)
    gx_touch = Column(Boolean, default=False)
    energiemeter = Column(String)

    # Accu
    accu_merk = Column(String)
    accu_type = Column(String)
    accu_capaciteit = Column(Float, default=0)

    # Back-up
    noodstroom = Column(Boolean, default=False)

    opmerkingen = Column(Text)

    project = relationship(
        "Project",
        backref="ess_configuratie",
    )