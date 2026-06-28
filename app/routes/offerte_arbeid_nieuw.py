from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offerteregels import create_arbeidregel

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get(
    "/offerte/{offerte_id}/arbeid/nieuw",
    response_class=HTMLResponse,
)
async def arbeid_nieuw(
    offerte_id: int,
    request: Request,
):

    return templates.TemplateResponse(
        request=request,
        name="offerte_arbeid_nieuw.html",
        context={
            "offerte_id": offerte_id,
        },
    )


@router.post("/offerte/{offerte_id}/arbeid/nieuw")
async def arbeid_opslaan(
    offerte_id: int,
    omschrijving: str = Form(...),
    uren: float = Form(...),
    uurtarief: float = Form(...),
    db: Session = Depends(get_db),
):

    create_arbeidregel(
        db,
        offerte_id,
        omschrijving,
        uren,
        uurtarief,
    )

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )