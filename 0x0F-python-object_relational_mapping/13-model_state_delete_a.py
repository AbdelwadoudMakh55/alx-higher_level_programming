#!/usr/bin/python3
""" This is the 13-model_state_delete_a module """

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    for obj in states:
        session.delete(obj)
    session.commit()
