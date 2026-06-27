from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.klant import Klant
from app.models.project import Project

router = APIRouter(prefix="/api")


@router.get("/search")
async def search(
    q: str,
    db: Session = Depends(get_db),
):

    resultaten = []

    # Klanten zoeken
    klanten = (
        db.query(Klant)
        .filter(
            Klant.actief == True,
            Klant.naam.ilike(f"%{q}%")
        )
        .limit(5)
        .all()
    )

    for klant in klanten:
        resultaten.append(
            {
                "type": "klant",
                "titel": klant.naam,
                "subtitel": klant.plaats or "",
                "url": f"/klanten/{klant.id}",
            }
        )

    # Projecten zoeken
    projecten = (
        db.query(Project)
        .filter(
            Project.actief == True,
            Project.naam.ilike(f"%{q}%")
        )
        .limit(5)
        .all()
    )

    for project in projecten:
        resultaten.append(
            {
                "type": "project",
                "titel": project.naam,
                "subtitel": project.projectnummer or "",
                "url": f"/project/{project.id}",
            }
        )

    return resultaten