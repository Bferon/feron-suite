from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.project import Project
from app.models.offerte import Offerte

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/{project_id}", response_class=HTMLResponse)
async def project_detail(
    project_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.actief == True,
        )
        .first()
    )

    if not project:
        return HTMLResponse(
            "Project niet gevonden.",
            status_code=404,
        )

    offertes = (
        db.query(Offerte)
        .filter(
            Offerte.project_id == project.id,
            Offerte.actief == True,
        )
        .order_by(Offerte.id.desc())
        .all()
    )

    totale_offertewaarde = (
        db.query(func.sum(Offerte.totaal))
        .filter(
            Offerte.project_id == project.id,
            Offerte.actief == True,
        )
        .scalar()
        or 0
    )

    aantal_offertes = len(offertes)

    return templates.TemplateResponse(
        request=request,
        name="project_detail.html",
        context={
            "project": project,
            "offertes": offertes,
            "aantal_offertes": aantal_offertes,
            "totale_offertewaarde": totale_offertewaarde,
        },
    )