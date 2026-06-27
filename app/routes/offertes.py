from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offertes import get_alle_offertes

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/offertes", response_class=HTMLResponse)
async def offertes(
    request: Request,
    db: Session = Depends(get_db),
):

    offertes = get_alle_offertes(db)

    return templates.TemplateResponse(
        request=request,
        name="offertes.html",
        context={
            "offertes": offertes,
        },
    )