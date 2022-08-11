#!/usr/bin/python3
"""
Script that lists all State objects from the db
and takes 3 arguments, result needs to be sorted
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    for st in session().query(State).order_by(State.id):
        print("{}: {}".format(st.id, st.name))
    session().close()
