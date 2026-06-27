from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.instellingen import (
    get_instellingen,
    update_instellingen,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/instellingen", response_class=HTMLResponse)
async def instellingen(
    request: Request,
    db: Session = Depends(get_db),
):

    instellingen = get_instellingen(db)

    return templates.TemplateResponse(
        request=request,
        name="instellingen.html",
        context={
            "instellingen": instellingen,
        },
    )


@router.post("/instellingen")
async def instellingen_opslaan(
    request: Request,
    bedrijfsnaam: str = Form(...),
    adres: str = Form(""),
    postcode: str = Form(""),
    plaats: str = Form(""),
    telefoon: str = Form(""),
    email: str = Form(""),
    kvk: str = Form(""),
    btw_nummer: str = Form(""),
    uurtarief: float = Form(62.50),
    voorrijkosten: float = Form(35.00),
    btw_percentage: float = Form(21.00),
    winstmarge: float = Form(35.00),
    standaard_leverancier: str = Form(""),
    db: Session = Depends(get_db),
):

    update_instellingen(
        db,
        {
            "bedrijfsnaam": bedrijfsnaam,
            "adres": adres,
            "postcode": postcode,
            "plaats": plaats,
            "telefoon": telefoon,
            "email": email,
            "kvk": kvk,
            "btw_nummer": btw_nummer,
            "uurtarief": uurtarief,
            "voorrijkosten": voorrijkosten,
            "btw_percentage": btw_percentage,
            "winstmarge": winstmarge,
            "standaard_leverancier": standaard_leverancier,
        },
    )

    return RedirectResponse(
        "/instellingen",
        status_code=303,
    )