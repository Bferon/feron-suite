from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.materialen import (
    create_materiaal,
    get_materiaal,
    update_materiaal,
    archive_materiaal,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

CATEGORIEEN = [
    "ESS",
    "Meterkasten",
    "Laadpalen",
    "Kabels",
    "Beveiliging",
    "Schakelmateriaal",
    "Installatiemateriaal",
    "PV",
    "Gereedschap",
    "Overig",
]


@router.get("/materiaal/nieuw", response_class=HTMLResponse)
async def nieuw_materiaal(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="materiaal_nieuw.html",
        context={
            "categorieen": CATEGORIEEN,
        },
    )


@router.post("/materiaal/nieuw")
async def nieuw_materiaal_opslaan(
    categorie: str = Form(...),
    merk: str = Form(""),
    artikelnummer: str = Form(""),
    omschrijving: str = Form(...),
    leverancier: str = Form(""),
    inkoopprijs: float = Form(0),
    verkoopprijs: float = Form(0),
    eenheid: str = Form("st"),
    voorraad: int = Form(0),
    db: Session = Depends(get_db),
):

    create_materiaal(
        db,
        {
            "categorie": categorie,
            "merk": merk,
            "artikelnummer": artikelnummer,
            "omschrijving": omschrijving,
            "leverancier": leverancier,
            "inkoopprijs": inkoopprijs,
            "verkoopprijs": verkoopprijs,
            "eenheid": eenheid,
            "voorraad": voorraad,
        },
    )

    return RedirectResponse(
        "/materialen",
        status_code=303,
    )


@router.get("/materiaal/{materiaal_id}/bewerken", response_class=HTMLResponse)
async def materiaal_bewerken(
    materiaal_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    materiaal = get_materiaal(db, materiaal_id)

    if not materiaal:
        return HTMLResponse(
            "Materiaal niet gevonden",
            status_code=404,
        )

    return templates.TemplateResponse(
        request=request,
        name="materiaal_bewerken.html",
        context={
            "materiaal": materiaal,
            "categorieen": CATEGORIEEN,
        },
    )


@router.post("/materiaal/{materiaal_id}/bewerken")
async def materiaal_opslaan(
    materiaal_id: int,
    categorie: str = Form(...),
    merk: str = Form(""),
    artikelnummer: str = Form(""),
    omschrijving: str = Form(...),
    leverancier: str = Form(""),
    inkoopprijs: float = Form(0),
    verkoopprijs: float = Form(0),
    eenheid: str = Form("st"),
    voorraad: int = Form(0),
    db: Session = Depends(get_db),
):

    update_materiaal(
        db,
        materiaal_id,
        {
            "categorie": categorie,
            "merk": merk,
            "artikelnummer": artikelnummer,
            "omschrijving": omschrijving,
            "leverancier": leverancier,
            "inkoopprijs": inkoopprijs,
            "verkoopprijs": verkoopprijs,
            "eenheid": eenheid,
            "voorraad": voorraad,
        },
    )

    return RedirectResponse(
        "/materialen",
        status_code=303,
    )


@router.get("/materiaal/{materiaal_id}/archiveer")
async def materiaal_archiveer(
    materiaal_id: int,
    db: Session = Depends(get_db),
):

    archive_materiaal(
        db,
        materiaal_id,
    )

    return RedirectResponse(
        "/materialen",
        status_code=303,
    )