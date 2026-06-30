from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.offerte_regel import OfferteRegel
from app.models.offerte import Offerte
from app.services.offerte_regel_service import OfferteRegelService

router = APIRouter()


@router.post("/offertes/{offerte_id}/regels/toevoegen")
async def regel_toevoegen(
    offerte_id: int,
    omschrijving: str = Form(...),
    aantal: float = Form(...),
    eenheid: str = Form(...),
    prijs: float = Form(...),
    korting: float = Form(0),
    db: Session = Depends(get_db),
):

    totaal = aantal * prijs
    totaal -= totaal * (korting / 100)

    regel = OfferteRegel(
        offerte_id=offerte_id,
        omschrijving=omschrijving,
        aantal=aantal,
        eenheid=eenheid,
        prijs=prijs,
        korting=korting,
        totaal=totaal,
    )

    db.add(regel)

    service = OfferteRegelService(db)

    offerte = (
        db.query(Offerte)
        .filter(Offerte.id == offerte_id)
        .first()
    )

    offerte.subtotaal = service.bereken_subtotaal(offerte_id)
    offerte.btw = service.bereken_btw(offerte_id)
    offerte.totaal = service.bereken_totaal(offerte_id)

    db.commit()

    return RedirectResponse(
        url=f"/offerte/{offerte_id}",
        status_code=303,
    )