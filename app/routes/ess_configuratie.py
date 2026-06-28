from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.ess_configuratie import get_configuratie

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/{project_id}/ess-configuratie", response_class=HTMLResponse)
async def ess_configuratie(
    project_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    configuratie = get_configuratie(
        db,
        project_id,
    )

    if not configuratie:
        return HTMLResponse(
            "Nog geen ESS configuratie gevonden.",
            status_code=404,
        )

    return templates.TemplateResponse(
        request=request,
        name="ess_configuratie.html",
        context={
            "configuratie": configuratie,
        },
    )