#!/usr/bin/python3
"""
Delete all State objects that have
the letter a in their name from hbtn_0e_6_usa
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
