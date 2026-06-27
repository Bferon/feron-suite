from sqlalchemy.orm import Session
from app.models.project import Project


def create_project(db: Session, data: dict):
    project = Project(**data)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_project(project_id: int, db: Session):
    return db.query(Project).filter(Project.id == project_id).first()


def get_projecten_van_klant(db: Session, klant_id: int):
    return (
        db.query(Project)
        .filter(
            Project.klant_id == klant_id,
            Project.actief == True,
        )
        .all()
    )


def update_project(db: Session, project_id: int, data: dict):
    project = get_project(project_id, db)

    if not project:
        return None

    for key, value in data.items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project


def archive_project(db: Session, project_id: int):
    project = get_project(project_id, db)

    if not project:
        return None

    project.actief = False

    db.commit()

    return project


def restore_project(db: Session, project_id: int):
    project = get_project(project_id, db)

    if not project:
        return None

    project.actief = True

    db.commit()

    return project