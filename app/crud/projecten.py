from sqlalchemy.orm import Session
from app.models.project import Project


def create_project(db: Session, data: dict):
    project = Project(**data)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projecten_van_klant(db: Session, klant_id: int):
    return db.query(Project).filter(Project.klant_id == klant_id).all()