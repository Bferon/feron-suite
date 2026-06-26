from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.klant import Klant
from app.crud.klanten import create_klant

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/klanten", response_class=HTMLResponse)
async def klanten(request: Request, db: Session = Depends(get_db)):
    klanten = db.query(Klant).all()

    return templates.TemplateResponse(
        request=request,
        name="klanten.html",
        context={
            "klanten": klanten
        }
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