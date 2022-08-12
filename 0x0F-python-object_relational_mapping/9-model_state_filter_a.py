#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a' from the
database hbtn_0e_6_usa and should take 3 arguments
results must be sorted in ascending order by states.id
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
    for state in session().query(State)\
            .filter(State.name.like('%a%'))\
            .order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session().close()
