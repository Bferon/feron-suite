from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offertes import get_offerte

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/offerte/{offerte_id}", response_class=HTMLResponse)
async def offerte_detail(
    offerte_id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    offerte = get_offerte(db, offerte_id)

    if not offerte:
        return HTMLResponse(
            "Offerte niet gevonden.",
            status_code=404,
        )

    return templates.TemplateResponse(
        request=request,
        name="offerte_detail.html",
        context={
            "offerte": offerte,
        },
    )