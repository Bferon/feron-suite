from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.klant import Klant

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/klanten/{klant_id}", response_class=HTMLResponse)
async def klant_detail(
    klant_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    klant = db.query(Klant).filter(Klant.id == klant_id).first()

    if not klant:
        return HTMLResponse("Klant niet gevonden", status_code=404)

    return templates.TemplateResponse(
        request=request,
        name="klant_detail.html",
        context={
            "klant": klant
        }
    )