from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.offerteregels import (
    get_offerteregel,
    delete_offerteregel,
)

router = APIRouter()


@router.get("/offerteregel/{regel_id}/verwijderen")
async def offerteregel_verwijderen(
    regel_id: int,
    db: Session = Depends(get_db),
):

    regel = get_offerteregel(
        db,
        regel_id,
    )

    if not regel:
        return RedirectResponse(
            "/offertes",
            status_code=303,
        )

    offerte_id = regel.offerte_id

    delete_offerteregel(
        db,
        regel_id,
    )

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )