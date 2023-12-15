#!/usr/bin/python3
""" This is the 10-model_state_my_get module """

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
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    new_loui = session.query(State).filter_by(name='Louisiana').first()
    print(new_loui.id)
    session.commit()
