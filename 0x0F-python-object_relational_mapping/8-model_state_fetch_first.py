#!/usr/bin/python3
""" This is the 8-model_state_fetch_first module """

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    f_state = session.query(State).order_by(State.id).first()
    if f_state:
        print(f"{f_state.id}: {f_state.name}")
    else:
        print("Nothing")
