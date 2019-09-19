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
class ChtzUser(Base):
    __tablename__ = 'chtz_user'

    uid = Column(Integer, primary_key=True)
    uuid = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)

    def __repr__(self):
        return str(self.__dict__)


class ProductPositionDetail(Base):
    __tablename__ = 'product_position_detail'

    date = Column(Date, primary_key=True)
    chuheyihao = Column(String, nullable=True)
    lianghuayihao = Column(String, nullable=True)

    def __repr__(self):
        return str(self.__dict__)


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


class CctvContent(Base):
    __tablename__ = 'cctv_content'

    date = Column(Date, primary_key=True)
    no1 = Column(BigInteger, nullable=True)
    no2  = Column(BigInteger, nullable=True)
    no3  = Column(BigInteger, nullable=True)
    no4  = Column(BigInteger, nullable=True)
    no5  = Column(BigInteger, nullable=True)
    no6  = Column(BigInteger, nullable=True)
    no7  = Column(BigInteger, nullable=True)
    return_500_next_week = Column(Float, nullable=True)
    no1_score  = Column(Float, nullable=True)
    no2_score  = Column(Float, nullable=True)
    no3_score  = Column(Float, nullable=True)
    no4_score  = Column(Float, nullable=True)
    no5_score  = Column(Float, nullable=True)
    no6_score  = Column(Float, nullable=True)
    no7_score  = Column(Float, nullable=True)
    no1_mean  = Column(Float, nullable=True)
    no2_mean  = Column(Float, nullable=True)
    no3_mean  = Column(Float, nullable=True)
    no4_mean  = Column(Float, nullable=True)
    no5_mean  = Column(Float, nullable=True)
    no6_mean  = Column(Float, nullable=True)
    no7_mean  = Column(Float, nullable=True)

    def __repr__(self):
        return str(self.__dict__)


class CctvTitle(Base):
    __tablename__ = 'cctv_title'

    date = Column(Date, primary_key=True)
    no1 = Column(BigInteger, nullable=True)
    no2  = Column(BigInteger, nullable=True)
    no3  = Column(BigInteger, nullable=True)
    no4  = Column(BigInteger, nullable=True)
    no5  = Column(BigInteger, nullable=True)
    no6  = Column(BigInteger, nullable=True)
    no7  = Column(BigInteger, nullable=True)
    return_500_next_week = Column(Float, nullable=True)
    no1_score  = Column(Float, nullable=True)
    no2_score  = Column(Float, nullable=True)
    no3_score  = Column(Float, nullable=True)
    no4_score  = Column(Float, nullable=True)
    no5_score  = Column(Float, nullable=True)
    no6_score  = Column(Float, nullable=True)
    no7_score  = Column(Float, nullable=True)
    no1_mean  = Column(Float, nullable=True)
    no2_mean  = Column(Float, nullable=True)
    no3_mean  = Column(Float, nullable=True)
    no4_mean  = Column(Float, nullable=True)
    no5_mean  = Column(Float, nullable=True)
    no6_mean  = Column(Float, nullable=True)
    no7_mean  = Column(Float, nullable=True)

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