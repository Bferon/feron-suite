from sqlalchemy.orm import Session

from app.models.offerte_regel import OfferteRegel


class OfferteRegelService:

    def __init__(self, db: Session):
        self.db = db

    def get_regels(self, offerte_id: int):
        return (
            self.db.query(OfferteRegel)
            .filter(
                OfferteRegel.offerte_id == offerte_id
            )
            .order_by(OfferteRegel.id)
            .all()
        )

    def bereken_subtotaal(self, offerte_id: int) -> float:

        regels = self.get_regels(offerte_id)

        return sum(regel.totaal for regel in regels)

    def bereken_btw(self, offerte_id: int) -> float:

        return self.bereken_subtotaal(offerte_id) * 0.21

    def bereken_totaal(self, offerte_id: int) -> float:

        return (
            self.bereken_subtotaal(offerte_id)
            + self.bereken_btw(offerte_id)
        )