from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.factuur_service import FactuurService

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/facturen", response_class=HTMLResponse)
async def facturen(
    request: Request,
    db: Session = Depends(get_db),
):

    service = FactuurService(db)

    return templates.TemplateResponse(
        request=request,
        name="facturen.html",
        context={
            "facturen": service.get_facturen(),
        },
    )


@router.get("/facturen/{factuur_id}", response_class=HTMLResponse)
async def factuur(
    factuur_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    service = FactuurService(db)

    factuur = service.get_factuur(factuur_id)

    return templates.TemplateResponse(
        request=request,
        name="factuur.html",
        context={
            "factuur": factuur,
        },
    )