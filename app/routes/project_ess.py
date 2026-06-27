from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.projecten import get_project

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/{project_id}/ess", response_class=HTMLResponse)
async def project_ess(
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
        name="project_ess.html",
        context={
            "project": project,
        },
    )