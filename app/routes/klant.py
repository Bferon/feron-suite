from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.klant import Klant
from app.models.project import Project
from app.models.offerte import Offerte

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/klanten/{klant_id}", response_class=HTMLResponse)
async def klant_detail(
    klant_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    klant = (
        db.query(Klant)
        .filter(
            Klant.id == klant_id,
            Klant.actief == True,
        )
        .first()
    )

    if not klant:
        return HTMLResponse(
            "Klant niet gevonden",
            status_code=404,
        )

    projecten = (
        db.query(Project)
        .filter(
            Project.klant_id == klant.id,
            Project.actief == True,
        )
        .order_by(Project.id.desc())
        .all()
    )

    offertes = (
        db.query(Offerte)
        .filter(
            Offerte.klant_id == klant.id,
            Offerte.actief == True,
        )
        .order_by(Offerte.id.desc())
        .all()
    )

    totale_projectwaarde = (
        db.query(func.sum(Project.offertebedrag))
        .filter(
            Project.klant_id == klant.id,
            Project.actief == True,
        )
        .scalar()
        or 0
    )

    return templates.TemplateResponse(
        request=request,
        name="klant_detail.html",
        context={
            "klant": klant,
            "projecten": projecten,
            "offertes": offertes,
            "totale_projectwaarde": totale_projectwaarde,
        },
    )