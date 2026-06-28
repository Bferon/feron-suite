from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.crud.offertes import create_offerte

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/offerte/nieuw", response_class=HTMLResponse)
async def offerte_nieuw(
    request: Request,
    db: Session = Depends(get_db),
):

    projecten = (
        db.query(Project)
        .filter(Project.actief == True)
        .order_by(Project.projectnummer)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="offerte_select_project.html",
        context={
            "projecten": projecten,
        },
    )


@router.post("/offerte/nieuw")
async def offerte_nieuw_opslaan(
    project_id: int = Form(...),
    db: Session = Depends(get_db),
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    offerte = create_offerte(
        db,
        {
            "klant_id": project.klant_id,
            "project_id": project.id,
            "status": "Concept",
        },
    )

    return RedirectResponse(
        url=f"/offerte/{offerte.id}",
        status_code=303,
    )