from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
# from . import crud, models, schemas, database
# from crud import crud
# from models import models
# from schemas import schemas
# from database import database
import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Visual Inspection System API"}

@app.post("/inspection_stations/", response_model=schemas.InspectionStation)
def create_inspection_station(station: schemas.InspectionStationCreate, db: Session = Depends(database.get_db)):
    return crud.create_inspection_station(db=db, station=station)

@app.get("/inspection_stations/", response_model=List[schemas.InspectionStation])
def read_inspection_stations(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_inspection_stations(db, skip=skip, limit=limit)

@app.get("/inspection_stations/{station_id}", response_model=schemas.InspectionStation)
def read_inspection_station(station_id: int, db: Session = Depends(database.get_db)):
    db_station = crud.get_inspection_station(db, station_id=station_id)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Station not found")
    return db_station

@app.post("/inspections/", response_model=schemas.Inspection)
def create_inspection(inspection: schemas.InspectionCreate, db: Session = Depends(database.get_db)):
    return crud.create_inspection(db=db, inspection=inspection)

# @app.get("/inspections/", response_model=List[schemas.Inspection])
# def read_inspections(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
#     return crud.get_inspections(db, skip=skip, limit=limit)

@app.get("/inspections/", response_model=List[schemas.Inspection])
def read_inspections(station_id: Optional[int] = None, product: Optional[str] = None, skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    query = db.query(models.Inspection)
    if station_id:
        query = query.filter(models.Inspection.station_id == station_id)
    if product:
        query = query.join(models.InspectionStation).filter(models.InspectionStation.product == product)
    return query.offset(skip).limit(limit).all()

@app.get("/inspections/{inspection_id}", response_model=schemas.Inspection)
def read_inspection(inspection_id: int, db: Session = Depends(database.get_db)):
    db_inspection = crud.get_inspection(db, inspection_id=inspection_id)
    if db_inspection is None:
        raise HTTPException(status_code=404, detail="Inspection not found")
    return db_inspection
