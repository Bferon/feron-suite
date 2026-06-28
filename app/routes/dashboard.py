from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db

from app.models.klant import Klant
from app.models.project import Project
from app.models.materiaal import Materiaal
from app.models.offerte import Offerte

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    db: Session = Depends(get_db),
):

    actieve_klanten = (
        db.query(Klant)
        .filter(Klant.actief == True)
        .count()
    )

    actieve_projecten = (
        db.query(Project)
        .filter(Project.actief == True)
        .count()
    )

    actieve_offertes = (
        db.query(Offerte)
        .filter(Offerte.actief == True)
        .count()
    )

    aantal_materialen = (
        db.query(Materiaal)
        .filter(Materiaal.actief == True)
        .count()
    )

    totale_offertewaarde = (
    db.query(func.sum(Project.offertebedrag))
    .filter(Project.actief == True)
    .scalar()
    or 0
    
    )

    ess_projecten = (
        db.query(Project)
        .filter(
            Project.actief == True,
            Project.type == "ESS",
        )
        .count()
    )

    meterkast_projecten = (
        db.query(Project)
        .filter(
            Project.actief == True,
            Project.type == "Meterkast",
        )
        .count()
    )

    laadpaal_projecten = (
        db.query(Project)
        .filter(
            Project.actief == True,
            Project.type == "Laadpaal",
        )
        .count()
    )

    laatste_projecten = (
        db.query(Project)
        .filter(Project.actief == True)
        .order_by(Project.id.desc())
        .limit(5)
        .all()
    )

    laatste_offertes = (
        db.query(Offerte)
        .filter(Offerte.actief == True)
        .order_by(Offerte.id.desc())
        .limit(5)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "actieve_klanten": actieve_klanten,
            "actieve_projecten": actieve_projecten,
            "actieve_offertes": actieve_offertes,
            "aantal_materialen": aantal_materialen,
            "totale_offertewaarde": totale_offertewaarde,
            "ess_projecten": ess_projecten,
            "meterkast_projecten": meterkast_projecten,
            "laadpaal_projecten": laadpaal_projecten,
            "laatste_projecten": laatste_projecten,
            "laatste_offertes": laatste_offertes,
        },
    )