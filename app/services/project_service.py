from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectService:
    """
    Alle logica rondom projecten.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_actieve_projecten(self):
        return (
            self.db.query(Project)
            .filter(Project.actief == True)
            .order_by(Project.id.desc())
            .all()
        )

    def get_laatste_projecten(self, aantal: int = 5):
        return (
            self.db.query(Project)
            .filter(Project.actief == True)
            .order_by(Project.id.desc())
            .limit(aantal)
            .all()
        )

    def get_project(self, project_id: int):
        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def aantal_actieve_projecten(self):
        return (
            self.db.query(Project)
            .filter(Project.actief == True)
            .count()
        )

    def aantal_ess_projecten(self):
        return (
            self.db.query(Project)
            .filter(
                Project.actief == True,
                Project.type == "ESS",
            )
            .count()
        )

    def aantal_meterkast_projecten(self):
        return (
            self.db.query(Project)
            .filter(
                Project.actief == True,
                Project.type == "Meterkast",
            )
            .count()
        )

    def aantal_laadpaal_projecten(self):
        return (
            self.db.query(Project)
            .filter(
                Project.actief == True,
                Project.type == "Laadpaal",
            )
            .count()
        )