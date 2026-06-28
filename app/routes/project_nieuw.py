from typing import Optional

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.projecten import create_project
from app.models.klant import Klant

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/nieuw", response_class=HTMLResponse)
async def nieuw_project(
    request: Request,
    klant_id: Optional[int] = None,
    db: Session = Depends(get_db),
):

    klanten = (
        db.query(Klant)
        .filter(Klant.actief == True)
        .order_by(Klant.naam)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="project_nieuw.html",
        context={
            "klant_id": klant_id,
            "klanten": klanten,
        },
    )


@router.post("/project/nieuw")
async def nieuw_project_opslaan(
    klant_id: int = Form(...),
    naam: str = Form(...),
    type: str = Form(...),
    status: str = Form(...),
    db: Session = Depends(get_db),
):

    project = create_project(
        db,
        {
            "klant_id": klant_id,
            "naam": naam,
            "type": type,
            "status": status,
        },
    )

    return RedirectResponse(
        url=f"/project/{project.id}",
        status_code=303,
    )