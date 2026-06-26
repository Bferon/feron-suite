from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/projecten", response_class=HTMLResponse)
async def projecten(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="projecten.html",
        context={}
    )