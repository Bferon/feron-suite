from sqlalchemy.orm import Session

from app.models.offerte import Offerte


class OfferteService:

    def __init__(self, db: Session):
        self.db = db

    def get_offertes(self):
        return (
            self.db.query(Offerte)
            .filter(Offerte.actief == True)
            .order_by(Offerte.id.desc())
            .all()
        )

    def get_offerte(self, offerte_id: int):
        return (
            self.db.query(Offerte)
            .filter(Offerte.id == offerte_id)
            .first()
        )

    def get_laatste_offertes(self, aantal: int = 5):
        return (
            self.db.query(Offerte)
            .filter(Offerte.actief == True)
            .order_by(Offerte.id.desc())
            .limit(aantal)
            .all()
        )

    def aantal_offertes(self):
        return (
            self.db.query(Offerte)
            .filter(Offerte.actief == True)
            .count()
        )