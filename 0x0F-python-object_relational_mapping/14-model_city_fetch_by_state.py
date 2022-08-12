#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
Your script should take 3 arguments
"""
from sys import argv
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)

from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    my_query = session.query(State, City)\
                      .filter(State.id == City.state_id)\
                      .order_by(City.id)\
                      .all()
    for state, city in my_query:
        print("{}: ({}) {}".format(state.name,
                                   city.id,
                                   city.name))
    session.close()
