from sqlalchemy import Column, String, Integer
from DataModel.base import Base


class Airport(Base):
    __tablename__ = 'airports'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)

    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city