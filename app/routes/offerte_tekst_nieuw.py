from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offerteregels import create_tekstregel

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get(
    "/offerte/{offerte_id}/tekst/nieuw",
    response_class=HTMLResponse,
)
async def tekst_nieuw(
    offerte_id: int,
    request: Request,
):

    return templates.TemplateResponse(
        request=request,
        name="offerte_tekst_nieuw.html",
        context={
            "offerte_id": offerte_id,
        },
    )


@router.post("/offerte/{offerte_id}/tekst/nieuw")
async def tekst_opslaan(
    offerte_id: int,
    omschrijving: str = Form(...),
    db: Session = Depends(get_db),
):

    create_tekstregel(
        db,
        offerte_id,
        omschrijving,
    )

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )