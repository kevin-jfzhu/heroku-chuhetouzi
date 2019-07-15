import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

"""                Header ends here                 """


class Restaurant(Base):
    __tablename__ = 'chuheyihao'

    name = Column(String(80), nullable=False)
    id = Column(Date, primary_key=True)


"""                 Init the database               """

engine = create_engine('sqlite:///restaurant_menu.db')

Base.metadata.create_all(engine)
