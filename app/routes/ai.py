from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.ai_service import analyseer_werkzaamheden

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/ai", response_class=HTMLResponse)
async def ai_calculator(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="ai.html",
        context={
            "resultaat": None,
            "omschrijving": "",
        },
    )


@router.post("/ai", response_class=HTMLResponse)
async def ai_berekenen(
    request: Request,
    omschrijving: str = Form(...),
):

    resultaat = analyseer_werkzaamheden(omschrijving)

    return templates.TemplateResponse(
        request=request,
        name="ai.html",
        context={
            "resultaat": resultaat,
            "omschrijving": omschrijving,
        },
    )