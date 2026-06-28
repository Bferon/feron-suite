from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offertes import (
    verzend_offerte,
    accepteer_offerte,
    wijs_offerte_af,
)

router = APIRouter()


@router.get("/offerte/{offerte_id}/verzenden")
async def offerte_verzenden(
    offerte_id: int,
    db: Session = Depends(get_db),
):

    verzend_offerte(
        db,
        offerte_id,
    )

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )


@router.get("/offerte/{offerte_id}/accepteren")
async def offerte_accepteren(
    offerte_id: int,
    db: Session = Depends(get_db),
):

    accepteer_offerte(
        db,
        offerte_id,
    )

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )


@router.get("/offerte/{offerte_id}/afwijzen")
async def offerte_afwijzen(
    offerte_id: int,
    db: Session = Depends(get_db),
):

    wijs_offerte_af(
        db,
        offerte_id,
    )

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )