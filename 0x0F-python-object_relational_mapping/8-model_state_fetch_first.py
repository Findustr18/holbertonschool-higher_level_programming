#!/usr/bin/python3
"""
Script that that prints the first State object from the database hbtn_0e_6_usa
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
    my_query = session().query(State).first()
    if my_query:
        print("{}: {}".format(my_query.id, my_query.name))
    else:
        print("Nothing")
    session().close()
