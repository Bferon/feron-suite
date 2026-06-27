from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offerteregels import (
    get_offerteregel,
    update_offerteregel,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get(
    "/offerteregel/{regel_id}/bewerken",
    response_class=HTMLResponse,
)
async def offerteregel_bewerken(
    regel_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    regel = get_offerteregel(db, regel_id)

    if not regel:
        return HTMLResponse(
            "Regel niet gevonden",
            status_code=404,
        )

    return templates.TemplateResponse(
        request=request,
        name="offerteregel_bewerken.html",
        context={
            "regel": regel,
        },
    )


@router.post("/offerteregel/{regel_id}/bewerken")
async def offerteregel_opslaan(
    regel_id: int,
    aantal: float = Form(...),
    db: Session = Depends(get_db),
):

    regel = update_offerteregel(
        db,
        regel_id,
        aantal,
    )

    return RedirectResponse(
        url=f"/offerte/{regel.offerte_id}",
        status_code=303,
    )