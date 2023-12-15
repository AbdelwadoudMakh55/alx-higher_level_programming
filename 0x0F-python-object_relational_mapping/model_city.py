#!/usr/bin/python3
""" This is model_city module """


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ This is the City class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
