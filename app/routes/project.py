from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/project/{project_id}", response_class=HTMLResponse)
async def project_detail(project_id: int):
    return HTMLResponse(f"<h1>Project {project_id}</h1>")