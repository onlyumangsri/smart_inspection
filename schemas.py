from pydantic import BaseModel
from typing import List, Optional

class InspectionBase(BaseModel):
    image_url: str
    inspection_outcome: str
    station_id: int

class InspectionCreate(InspectionBase):
    pass

class Inspection(InspectionBase):
    id: int

    class Config:
        orm_mode = True

class InspectionStationBase(BaseModel):
    name: str
    description: str
    product: str
    criteria: str

class InspectionStationCreate(InspectionStationBase):
    pass

class InspectionStation(InspectionStationBase):
    id: int
    inspections: List[Inspection] = []

    class Config:
        orm_mode = True
