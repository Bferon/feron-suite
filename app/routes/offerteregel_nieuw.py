from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.materiaal import Materiaal
from app.crud.offerteregels import create_offerteregel

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/offerte/{offerte_id}/regel/nieuw", response_class=HTMLResponse)
async def nieuwe_offerteregel(
    offerte_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    materialen = (
        db.query(Materiaal)
        .filter(Materiaal.actief == True)
        .order_by(Materiaal.omschrijving)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="offerteregel_nieuw.html",
        context={
            "offerte_id": offerte_id,
            "materialen": materialen,
        },
    )


@router.post("/offerte/{offerte_id}/regel/nieuw")
async def nieuwe_offerteregel_opslaan(
    offerte_id: int,
    materiaal_id: int = Form(...),
    aantal: float = Form(...),
    db: Session = Depends(get_db),
):

    create_offerteregel(
        db,
        offerte_id,
        materiaal_id,
        aantal,
    )

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )