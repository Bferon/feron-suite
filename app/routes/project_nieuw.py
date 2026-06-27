from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.projecten import create_project

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/nieuw", response_class=HTMLResponse)
async def nieuw_project(
    request: Request,
    klant_id: int,
):
    return templates.TemplateResponse(
        request=request,
        name="project_nieuw.html",
        context={
            "klant_id": klant_id,
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
    create_project(
        db,
        {
            "klant_id": klant_id,
            "naam": naam,
            "type": type,
            "status": status,
        },
    )

    return RedirectResponse(
        url=f"/klanten/{klant_id}",
        status_code=303,
    )