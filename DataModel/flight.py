from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

from DataModel.base import Base


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    airline = Column(String)
    codeshare = Column(Boolean)
    stops = Column(Integer)
    equipment = Column(String)
    sourceAirportId = Column(Integer, ForeignKey('airports.id'))
    destinationAirportId = Column(Integer, ForeignKey('airports.id'))

    def __init__(self, id, airline, codeshare, stops, equipment, sourceAirportId, destinationAirportId):
        self.id = id
        self.airline = airline
        self.codeshare = codeshare
        self.stops = stops
        self.equipment = equipment
        self.sourceAirportId = sourceAirportId
        self.destinationAirportId = destinationAirportId