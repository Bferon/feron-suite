from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.materialen import (
    get_materialen,
    get_gearchiveerde_materialen,
    restore_materiaal,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/materialen", response_class=HTMLResponse)
async def materialen(
    request: Request,
    db: Session = Depends(get_db),
):

    return templates.TemplateResponse(
        request=request,
        name="materialen.html",
        context={
            "materialen": get_materialen(db),
        },
    )


@router.get("/materialen/archief", response_class=HTMLResponse)
async def materialen_archief(
    request: Request,
    db: Session = Depends(get_db),
):

    return templates.TemplateResponse(
        request=request,
        name="materialen_archief.html",
        context={
            "materialen": get_gearchiveerde_materialen(db),
        },
    )


@router.get("/materiaal/{materiaal_id}/herstellen")
async def materiaal_herstellen(
    materiaal_id: int,
    db: Session = Depends(get_db),
):

    restore_materiaal(
        db,
        materiaal_id,
    )

    return RedirectResponse(
        "/materialen/archief",
        status_code=303,
    )