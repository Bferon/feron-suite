from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/ai", response_class=HTMLResponse)
async def ai_calculator(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="ai.html",
        context={}
    )