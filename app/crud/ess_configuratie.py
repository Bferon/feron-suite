from sqlalchemy.orm import Session

from app.models.ess_configuratie import EssConfiguratie


def create_configuratie(
    db: Session,
    project_id: int,
):

    configuratie = EssConfiguratie(
        project_id=project_id,
    )

    db.add(configuratie)
    db.commit()
    db.refresh(configuratie)

    return configuratie


def get_configuratie(
    db: Session,
    project_id: int,
):

    return (
        db.query(EssConfiguratie)
        .filter(
            EssConfiguratie.project_id == project_id
        )
        .first()
    )


def get_or_create_configuratie(
    db: Session,
    project_id: int,
):

    configuratie = get_configuratie(
        db,
        project_id,
    )

    if configuratie:
        return configuratie

    return create_configuratie(
        db,
        project_id,
    )


def update_configuratie(
    db: Session,
    project_id: int,
    data: dict,
):

    configuratie = get_or_create_configuratie(
        db,
        project_id,
    )

    for key, value in data.items():

        if hasattr(configuratie, key):
            setattr(
                configuratie,
                key,
                value,
            )

    db.commit()
    db.refresh(configuratie)

    return configuratie


def delete_configuratie(
    db: Session,
    project_id: int,
):

    configuratie = get_configuratie(
        db,
        project_id,
    )

    if not configuratie:
        return False

    db.delete(configuratie)
    db.commit()

    return True


def save_advies(
    db: Session,
    project_id: int,
    advies: dict,
):

    configuratie = get_or_create_configuratie(
        db,
        project_id,
    )

    configuratie.multiplus = advies.get("multiplus")
    configuratie.accu_type = advies.get("accu")
    configuratie.energiemeter = advies.get("energiemeter")

    if advies.get("cerbo"):
        configuratie.cerbo_gx = True

    if advies.get("gx_touch"):
        configuratie.gx_touch = True

    db.commit()
    db.refresh(configuratie)

    return configuratie