from datetime import date

from sqlalchemy.orm import Session

from app.models.factuur import Factuur


class FactuurService:

    def __init__(self, db: Session):
        self.db = db

    def get_facturen(self):
        return (
            self.db.query(Factuur)
            .filter(Factuur.actief == True)
            .order_by(Factuur.id.desc())
            .all()
        )

    def get_factuur(self, factuur_id: int):
        return (
            self.db.query(Factuur)
            .filter(Factuur.id == factuur_id)
            .first()
        )

    def get_laatste_facturen(self, aantal: int = 10):
        return (
            self.db.query(Factuur)
            .filter(Factuur.actief == True)
            .order_by(Factuur.id.desc())
            .limit(aantal)
            .all()
        )

    def nieuw_factuurnummer(self) -> str:

        jaar = date.today().year

        laatste = (
            self.db.query(Factuur)
            .order_by(Factuur.id.desc())
            .first()
        )

        if laatste is None:
            nummer = 1
        else:
            try:
                nummer = int(laatste.factuurnummer.split("-")[1]) + 1
            except Exception:
                nummer = laatste.id + 1

        return f"F{jaar}-{nummer:04d}"