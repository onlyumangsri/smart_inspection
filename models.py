from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class InspectionStation(Base):
    __tablename__ = 'inspection_stations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    product = Column(String)
    criteria = Column(String)
    inspections = relationship("Inspection", back_populates="station")

class Inspection(Base):
    __tablename__ = 'inspections'
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey('inspection_stations.id'))
    image_url = Column(String)
    inspection_outcome = Column(String)
    station = relationship("InspectionStation", back_populates="inspections")
