from datetime import datetime

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.projecten import (
    get_project,
    update_project,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/{project_id}/bewerken", response_class=HTMLResponse)
async def project_bewerken(
    project_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    project = get_project(db, project_id)

    if not project:
        return HTMLResponse(
            "Project niet gevonden.",
            status_code=404,
        )

    return templates.TemplateResponse(
        request=request,
        name="project_bewerken.html",
        context={
            "project": project,
        },
    )


@router.post("/project/{project_id}/bewerken")
async def project_bewerken_opslaan(
    project_id: int,
    naam: str = Form(...),
    type: str = Form(...),
    status: str = Form(...),
    startdatum: str = Form(""),
    einddatum: str = Form(""),
    offertebedrag: float = Form(0),
    opmerkingen: str = Form(""),
    db: Session = Depends(get_db),
):

    update_project(
        db,
        project_id,
        {
            "naam": naam,
            "type": type,
            "status": status,
            "startdatum": datetime.strptime(startdatum, "%Y-%m-%d").date()
            if startdatum else None,
            "einddatum": datetime.strptime(einddatum, "%Y-%m-%d").date()
            if einddatum else None,
            "offertebedrag": offertebedrag,
            "opmerkingen": opmerkingen,
        },
    )

    return RedirectResponse(
        url=f"/project/{project_id}",
        status_code=303,
    )