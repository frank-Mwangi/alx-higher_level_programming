#!/usr/bin/python3
"""
List all State objects from hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
