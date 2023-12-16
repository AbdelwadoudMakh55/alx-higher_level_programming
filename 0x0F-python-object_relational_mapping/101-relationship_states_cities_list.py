#!/usr/bin/python3
""" This is the 101-relationship_states_cities_list module """

import sys
from relationship_state import Base, State
from relationship_city import City

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
    states = session.query(State).order_by(State.id).all()
    for obj in states:
        print(f"{obj.id}: {obj.name}")
        for city in obj.cities:
            print(f"\t{city.id}: {city.name}")
