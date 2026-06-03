from app.database.db import SessionLocal
from app.database.models import (
    Tonnage,
    CargoVC,
    CargoTC
)


def get_vessels():

    db = SessionLocal()

    vessels = db.query(
        Tonnage
    ).all()

    db.close()

    return vessels


def get_vc_cargoes():

    db = SessionLocal()

    cargoes = db.query(
        CargoVC
    ).all()

    db.close()

    return cargoes


def get_tc_cargoes():

    db = SessionLocal()

    cargoes = db.query(
        CargoTC
    ).all()

    db.close()

    return cargoes