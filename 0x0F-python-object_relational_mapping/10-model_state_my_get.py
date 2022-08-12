#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa and should take 4 arguments
results must be sorted in ascending order by states.id
"""
from sys import argv
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
    my_query = session().query(State).filter_by(name=argv[4]).first()
    if my_query:
        print("{}".format(my_query.id))
    else:
        print("Not found")
    session().close()
