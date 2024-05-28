from sqlalchemy.orm import Session
# from . import models, schemas
import models
import schemas

def get_inspection_station(db: Session, station_id: int):
    return db.query(models.InspectionStation).filter(models.InspectionStation.id == station_id).first()

def get_inspection_stations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.InspectionStation).offset(skip).limit(limit).all()

def create_inspection_station(db: Session, station: schemas.InspectionStationCreate):
    db_station = models.InspectionStation(**station.dict())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

def get_inspection(db: Session, inspection_id: int):
    return db.query(models.Inspection).filter(models.Inspection.id == inspection_id).first()

def get_inspections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Inspection).offset(skip).limit(limit).all()

def create_inspection(db: Session, inspection: schemas.InspectionCreate):
    db_inspection = models.Inspection(**inspection.dict())
    db.add(db_inspection)
    db.commit()
    db.refresh(db_inspection)
    return db_inspection
