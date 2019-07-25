import sys
import os
import psycopg2 as pg2
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

"""                Header ends here                 """


class ProductPerformance(Base):
    __tablename__ = 'product_performance'

    date = Column(Date, primary_key=True)
    product_name = Column(String, primary_key=True)
    last_updated_time = Column(BigInteger, nullable=False)

    unit_value = Column(Float, nullable=True)
    asset_value = Column(Float, nullable=True)
    unit_value_change = Column(Float, nullable=True)
    asset_value_change = Column(Float, nullable=True)
    shares = Column(Float, nullable=True)
    note_of_important_events = Column(String, nullable=True)

    def __repr__(self):
        return str(self.__dict__)


class StrategyPerformance(Base):
    __tablename__ = 'strategy_performance'

    subclass_name = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)
    last_updated_time = Column(BigInteger, nullable=False)
    strategy_value = Column(Float, nullable=True)
    holding_shares = Column(Float, nullable=True)
    signal_direction = Column(Integer, nullable=True)
    correct_direction = Column(Integer, nullable=True)
    rolling_accuracy = Column(Float, nullable=True)
    trailing_drawdown = Column(Float, nullable=True)
    note_of_important_events = Column(String, nullable=True)

    def __repr__(self):
        return str(self.__dict__)


"""                 Init the database               """

LOCAL_DB = 'postgresql://kevinzhu:Mcgrady1@127.0.0.1:5432/mydb'
DATABASE_URL = os.environ.get('DATABASE_URL')
NEW_DB_URL = os.environ.get('HEROKU_POSTGRESQL_MAROON_URL')


engine = create_engine(NEW_DB_URL.replace('postgres', 'postgresql+psycopg2')+'?sslmode=require')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
