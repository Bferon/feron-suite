from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offertes import create_offerte
from app.crud.projecten import get_project

router = APIRouter()


@router.get("/project/{project_id}/offerte/nieuw")
async def nieuwe_offerte(
    project_id: int,
    db: Session = Depends(get_db),
):

    project = get_project(db, project_id)

    if not project:
        return RedirectResponse("/", status_code=303)

    offerte = create_offerte(
        db,
        {
            "klant_id": project.klant_id,
            "project_id": project.id,
            "status": "Concept",
        },
    )

    return RedirectResponse(
        url=f"/offerte/{offerte.id}",
        status_code=303,
    )