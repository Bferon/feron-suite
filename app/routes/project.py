from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/{project_id}", response_class=HTMLResponse)
async def project_detail(
    project_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return HTMLResponse("Project niet gevonden", status_code=404)

    return templates.TemplateResponse(
        request=request,
        name="project_detail.html",
        context={
            "project": project,
        },
    )