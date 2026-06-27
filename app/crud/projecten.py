from datetime import datetime

from sqlalchemy.orm import Session

from app.models.project import Project


def generate_projectnummer(db: Session):
    jaar = datetime.now().year

    projecten = (
        db.query(Project)
        .filter(Project.projectnummer.like(f"{jaar}-%"))
        .all()
    )

    hoogste_nummer = 0

    for project in projecten:

        if not project.projectnummer:
            continue

        try:
            nummer = int(project.projectnummer.split("-")[1])

            if nummer > hoogste_nummer:
                hoogste_nummer = nummer

        except (IndexError, ValueError):
            continue

    nieuw_nummer = hoogste_nummer + 1

    return f"{jaar}-{nieuw_nummer:04d}"


def create_project(db: Session, data: dict):

    data["projectnummer"] = generate_projectnummer(db)

    project = Project(**data)

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_project(db: Session, project_id: int):

    return (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )


def get_projecten_van_klant(db: Session, klant_id: int):

    return (
        db.query(Project)
        .filter(
            Project.klant_id == klant_id,
            Project.actief == True,
        )
        .order_by(Project.projectnummer.desc())
        .all()
    )


def get_alle_projecten(db: Session):

    return (
        db.query(Project)
        .filter(Project.actief == True)
        .order_by(Project.projectnummer.desc())
        .all()
    )


def update_project(db: Session, project_id: int, data: dict):

    project = get_project(db, project_id)

    if not project:
        return None

    for key, value in data.items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project


def archive_project(db: Session, project_id: int):

    project = get_project(db, project_id)

    if not project:
        return None

    project.actief = False

    db.commit()

    return project


def restore_project(db: Session, project_id: int):

    project = get_project(db, project_id)

    if not project:
        return None

    project.actief = True

    db.commit()

    return project