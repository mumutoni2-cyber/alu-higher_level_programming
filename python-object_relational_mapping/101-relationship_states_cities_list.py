#!/usr/bin/python3
"""Lists all State objects and their corresponding City objects."""
import sys
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

try:
    import relationship_city
except ImportError:
    relationship_city = None

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
