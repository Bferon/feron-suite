from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.klant import Klant
from app.models.project import Project

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
        .order_by(Project.id.desc())
        .limit(5)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "actieve_klanten": actieve_klanten,
            "actieve_projecten": actieve_projecten,
            "ess_projecten": ess_projecten,
            "meterkast_projecten": meterkast_projecten,
            "laadpaal_projecten": laadpaal_projecten,
            "laatste_projecten": laatste_projecten,
        },
    )