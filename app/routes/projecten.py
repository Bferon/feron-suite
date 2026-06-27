from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project

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