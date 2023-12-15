#!/usr/bin/python3
""" This is model_state module """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, unique=True, nullable=False,
                autoincrement=True)
    name = Column("name", String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
