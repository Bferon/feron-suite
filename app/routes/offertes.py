from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.offerte import Offerte

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/offertes", response_class=HTMLResponse)
async def offertes(
    request: Request,
    db: Session = Depends(get_db),
):

    offertes = (
        db.query(Offerte)
        .filter(Offerte.actief == True)
        .order_by(Offerte.id.desc())
        .all()
    )

    return templates.TemplateResponse(
        "offertes.html",
        {
            "request": request,
            "offertes": offertes,
        },
    )


@router.get("/offerte/{offerte_id}", response_class=HTMLResponse)
async def offerte(
    offerte_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    offerte = (
        db.query(Offerte)
        .filter(Offerte.id == offerte_id)
        .first()
    )

    return templates.TemplateResponse(
        "offerte.html",
        {
            "request": request,
            "offerte": offerte,
        },
    )