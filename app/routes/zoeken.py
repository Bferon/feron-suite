from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database import get_db

from app.models.klant import Klant
from app.models.project import Project
from app.models.offerte import Offerte
from app.models.materiaal import Materiaal

router = APIRouter()


@router.get("/zoeken")
async def zoeken(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):

    zoekterm = f"%{q}%"

    klanten = (
        db.query(Klant)
        .filter(
            Klant.actief == True,
            or_(
                Klant.naam.like(zoekterm),
                Klant.plaats.like(zoekterm),
                Klant.email.like(zoekterm),
            ),
        )
        .limit(5)
        .all()
    )

    projecten = (
        db.query(Project)
        .filter(
            Project.actief == True,
            or_(
                Project.naam.like(zoekterm),
                Project.projectnummer.like(zoekterm),
            ),
        )
        .limit(5)
        .all()
    )

    offertes = (
        db.query(Offerte)
        .filter(
            Offerte.actief == True,
            Offerte.offertenummer.like(zoekterm),
        )
        .limit(5)
        .all()
    )

    materialen = (
        db.query(Materiaal)
        .filter(
            Materiaal.actief == True,
            Materiaal.omschrijving.like(zoekterm),
        )
        .limit(5)
        .all()
    )

    return {
        "klanten": [
            {
                "id": klant.id,
                "naam": klant.naam,
            }
            for klant in klanten
        ],
        "projecten": [
            {
                "id": project.id,
                "nummer": project.projectnummer,
                "naam": project.naam,
            }
            for project in projecten
        ],
        "offertes": [
            {
                "id": offerte.id,
                "nummer": offerte.offertenummer,
            }
            for offerte in offertes
        ],
        "materialen": [
            {
                "id": materiaal.id,
                "omschrijving": materiaal.omschrijving,
            }
            for materiaal in materialen
        ],
    }