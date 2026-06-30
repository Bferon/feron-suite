from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db

from app.models.project import Project

from app.services.dashboard_service import DashboardService
from app.services.offerte_service import OfferteService

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    db: Session = Depends(get_db),
):

    dashboard_service = DashboardService(db)
    offerte_service = OfferteService(db)

    stats = dashboard_service.get_stats()

    actieve_klanten = stats["actieve_klanten"]
    actieve_projecten = stats["actieve_projecten"]
    actieve_offertes = stats["actieve_offertes"]
    aantal_materialen = stats["aantal_materialen"]

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

    laatste_offertes = offerte_service.get_laatste_offertes()

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