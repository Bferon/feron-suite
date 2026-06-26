from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/project/nieuw", response_class=HTMLResponse)
async def nieuw_project(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="project_nieuw.html",
        context={}
    )