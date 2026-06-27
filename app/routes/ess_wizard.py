from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.models.ess_wizard import EssWizard

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/{project_id}/ess", response_class=HTMLResponse)
async def ess_wizard(
    project_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return HTMLResponse("Project niet gevonden", status_code=404)

    ess = (
        db.query(EssWizard)
        .filter(EssWizard.project_id == project_id)
        .first()
    )

    return templates.TemplateResponse(
        request=request,
        name="ess_wizard.html",
        context={
            "project": project,
            "ess": ess,
        },
    )


@router.post("/project/{project_id}/ess")
async def ess_opslaan(
    project_id: int,
    netaansluiting: str = Form(...),
    hoofdzekering: int = Form(...),
    jaarverbruik: float = Form(...),
    teruglevering: float = Form(...),
    db: Session = Depends(get_db),
):

    ess = (
        db.query(EssWizard)
        .filter(EssWizard.project_id == project_id)
        .first()
    )

    if not ess:

        ess = EssWizard(project_id=project_id)
        db.add(ess)

    ess.netaansluiting = netaansluiting
    ess.hoofdzekering = hoofdzekering
    ess.jaarverbruik = jaarverbruik
    ess.teruglevering = teruglevering

    db.commit()

    return RedirectResponse(
        f"/project/{project_id}",
        status_code=303,
    )