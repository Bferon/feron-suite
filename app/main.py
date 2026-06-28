from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine

# Database modellen
from app.models import (
    Klant,
    Project,
    Materiaal,
    Instellingen,
    EssConfiguratie,
    Offerte,
    OfferteRegel,
)

# Routes
from app.routes import dashboard
from app.routes import klanten
from app.routes import klant
from app.routes import projecten
from app.routes import project
from app.routes import project_nieuw
from app.routes import project_bewerken
from app.routes import projecten_archief
from app.routes import project_ess
from app.routes import ess_configuratie

from app.routes import offertes
from app.routes import offerte
from app.routes import offerte_nieuw
from app.routes import offerteregel_nieuw
from app.routes import offerte_arbeid_nieuw
from app.routes import offerte_tekst_nieuw
from app.routes import offerte_select_project
from app.routes import offerte_status
from app.routes import ess
from app.routes import ai
from app.routes import materialen
from app.routes import materiaal
from app.routes import instellingen
from app.routes import zoeken
from app.routes import offerteregel_nieuw
from app.routes import ess_wizard

from app.models import (
    Klant,
    Project,
    Materiaal,
    Instellingen,
    EssWizard,
)

# Database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Feron Suite"
)

# Static bestanden
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

# Dashboard
app.include_router(dashboard.router)

# CRM
app.include_router(klanten.router)
app.include_router(klant.router)
app.include_router(zoeken.router)


# Projecten
app.include_router(projecten.router)
app.include_router(project_nieuw.router)
app.include_router(project.router)
app.include_router(project_bewerken.router)
app.include_router(project_ess.router)
app.include_router(projecten_archief.router)



app.include_router(offertes.router)

app.include_router(offerte_select_project.router)

app.include_router(offerte_nieuw.router)

app.include_router(offerteregel_nieuw.router)
app.include_router(offerte_arbeid_nieuw.router)
app.include_router(offerte_tekst_nieuw.router)

app.include_router(offerte_status.router)

app.include_router(offerte.router)

# Installaties
app.include_router(ess.router)
app.include_router(ess_wizard.router)
app.include_router(ess_configuratie.router)

# AI
app.include_router(ai.router)

# Materialen
app.include_router(materialen.router)
app.include_router(materiaal.router)

# Instellingen
app.include_router(instellingen.router)

Base.metadata.create_all(bind=engine)