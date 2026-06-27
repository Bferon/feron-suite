from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.klant import Klant
from app.crud.klanten import (
    create_klant,
    get_klant,
    update_klant,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/klanten", response_class=HTMLResponse)
async def klanten(request: Request, db: Session = Depends(get_db)):
    klanten = (
        db.query(Klant)
        .filter(Klant.actief == True)
        .order_by(Klant.naam)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="klanten.html",
        context={"klanten": klanten},
    )


@router.get("/klanten/archief", response_class=HTMLResponse)
async def klanten_archief(request: Request, db: Session = Depends(get_db)):
    klanten = (
        db.query(Klant)
        .filter(Klant.actief == False)
        .order_by(Klant.naam)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="klanten_archief.html",
        context={"klanten": klanten},
    )


@router.post("/klanten")
async def nieuwe_klant(
    naam: str = Form(...),
    adres: str = Form(""),
    postcode: str = Form(""),
    plaats: str = Form(""),
    telefoon: str = Form(""),
    email: str = Form(""),
    db: Session = Depends(get_db),
):
    create_klant(
        db,
        {
            "naam": naam,
            "adres": adres,
            "postcode": postcode,
            "plaats": plaats,
            "telefoon": telefoon,
            "email": email,
        },
    )

    return RedirectResponse("/klanten", status_code=303)


@router.get("/klanten/{klant_id}/archiveer")
async def archiveer_klant(
    klant_id: int,
    db: Session = Depends(get_db),
):
    klant = get_klant(db, klant_id)

    if klant:
        klant.actief = False
        db.commit()

    return RedirectResponse("/klanten", status_code=303)


@router.get("/klanten/{klant_id}/herstel")
async def herstel_klant(
    klant_id: int,
    db: Session = Depends(get_db),
):
    klant = get_klant(db, klant_id)

    if klant:
        klant.actief = True
        db.commit()

    return RedirectResponse("/klanten/archief", status_code=303)


@router.get("/klanten/{klant_id}/bewerken", response_class=HTMLResponse)
async def klant_bewerken(
    klant_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    klant = get_klant(db, klant_id)

    if not klant:
        return HTMLResponse("Klant niet gevonden", status_code=404)

    return templates.TemplateResponse(
        request=request,
        name="klant_bewerken.html",
        context={"klant": klant},
    )


@router.post("/klanten/{klant_id}/bewerken")
async def klant_bewerken_opslaan(
    klant_id: int,
    naam: str = Form(...),
    adres: str = Form(""),
    postcode: str = Form(""),
    plaats: str = Form(""),
    telefoon: str = Form(""),
    email: str = Form(""),
    db: Session = Depends(get_db),
):
    update_klant(
        db,
        klant_id,
        {
            "naam": naam,
            "adres": adres,
            "postcode": postcode,
            "plaats": plaats,
            "telefoon": telefoon,
            "email": email,
        },
    )

    return RedirectResponse(
        url="/klanten",
        status_code=303,
    )