from app.database.db import SessionLocal
from app.database.models import (
    Email,
    Tonnage,
    CargoVC,
    CargoTC
)


def get_db():

    db = SessionLocal()

    try:
        return db

    finally:
        pass
    
    
def save_tonnage(vessel):

    db = SessionLocal()

    existing = db.query(Tonnage).filter(

        Tonnage.vessel_name == vessel["vessel_name"],

        Tonnage.open_port == vessel["open_port"],

        Tonnage.open_date == vessel["open_date"]

    ).first()

    if existing:

        print("Duplicate vessel found")

        db.close()

        return False

    row = Tonnage(

        vessel_name=vessel["vessel_name"],

        vessel_size=vessel["vessel_size"],

        open_port=vessel["open_port"],

        open_date=vessel["open_date"]
    )

    db.add(row)

    db.commit()

    db.close()

    return True
    
def save_vc(cargo):

    db = SessionLocal()

    existing = db.query(CargoVC).filter(

        CargoVC.cargo_name == cargo["cargo_name"],

        CargoVC.loading_port == cargo["loading_port"],

        CargoVC.discharge_port == cargo["discharge_port"],

        CargoVC.laycan == cargo["laycan"]

    ).first()

    if existing:

        print("Duplicate VC cargo found")

        db.close()

        return False

    row = CargoVC(

        account_name=cargo["account_name"],

        cargo_name=cargo["cargo_name"],

        loading_port=cargo["loading_port"],

        discharge_port=cargo["discharge_port"],

        laycan=cargo["laycan"],

        cargo_type=cargo["cargo_type"]
    )

    db.add(row)

    db.commit()

    db.close()

    return True
    
def save_tc(cargo):

    db = SessionLocal()

    existing = db.query(CargoTC).filter(

        CargoTC.delivery_port == cargo["delivery_port"],

        CargoTC.redelivery_port == cargo["redelivery_port"],

        CargoTC.duration == cargo["duration"],

        CargoTC.laycan == cargo["laycan"]

    ).first()

    if existing:

        print("Duplicate TC cargo found")

        db.close()

        return False

    row = CargoTC(

        account_name=cargo["account_name"],

        delivery_port=cargo["delivery_port"],

        redelivery_port=cargo["redelivery_port"],

        duration=cargo["duration"],

        laycan=cargo["laycan"]
    )

    db.add(row)

    db.commit()

    db.close()

    return True