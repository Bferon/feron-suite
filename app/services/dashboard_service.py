from sqlalchemy.orm import Session

from app.models.klant import Klant
from app.models.project import Project
from app.models.offerte import Offerte
from app.models.materiaal import Materiaal


class DashboardService:
    """
    Serviceklasse voor alle dashboardstatistieken.
    Deze klasse wordt in v0.8 gebruikt door dashboard.py.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_stats(self) -> dict:
        return {
            "actieve_klanten": (
                self.db.query(Klant)
                .filter(Klant.actief == True)
                .count()
            ),
            "actieve_projecten": (
                self.db.query(Project)
                .filter(Project.actief == True)
                .count()
            ),
            "actieve_offertes": (
                self.db.query(Offerte)
                .filter(Offerte.actief == True)
                .count()
            ),
            "aantal_materialen": (
                self.db.query(Materiaal)
                .filter(Materiaal.actief == True)
                .count()
            ),
        }