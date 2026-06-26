from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine

from app.routes import dashboard
from app.routes import klanten
from app.routes import projecten
from app.routes import ess
from app.routes import project_nieuw

# Alle database-tabellen aanmaken
from app.models import Klant
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feron Suite")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(dashboard.router)
app.include_router(klanten.router)
app.include_router(projecten.router)
app.include_router(ess.router)
app.include_router(project_nieuw.router)