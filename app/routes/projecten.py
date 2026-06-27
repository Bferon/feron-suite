from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.crud.projecten import (
    archive_project,
    restore_project,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/projecten", response_class=HTMLResponse)
async def projecten(
    request: Request,
    db: Session = Depends(get_db),
):

    projecten = (
        db.query(Project)
        .filter(Project.actief == True)
        .order_by(Project.id.desc())
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="projecten.html",
        context={
            "projecten": projecten,
        },
    )


@router.get("/projecten/{project_id}/archiveer")
async def project_archiveer(
    project_id: int,
    db: Session = Depends(get_db),
):

    archive_project(db, project_id)

    return RedirectResponse(
        "/projecten",
        status_code=303,
    )


@router.get("/projecten/{project_id}/herstel")
async def project_herstel(
    project_id: int,
    db: Session = Depends(get_db),
):

    restore_project(db, project_id)

    return RedirectResponse(
        "/projecten/archief",
        status_code=303,
    )