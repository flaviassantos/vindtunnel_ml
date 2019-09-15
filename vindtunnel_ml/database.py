from sqlalchemy import Column, Integer, String, Float
from sqlalchemy_utils import get_mapper
import mysql.connector
from contextlib import contextmanager
import pandas as pd

from vindtunnel_ml import Session, Base

pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)


class AlarmEvents(Base):
    __tablename__ = 'alarm_events'

    ID = Column(Integer, primary_key=True)
    GroupID = Column(Integer)
    GroupName = Column(String(20))
    DeviceID = Column(Integer)
    DeviceName = Column(String(20))
    IONum = Column(Integer)
    Type = Column(Integer)
    ChannelName = Column(String(20))
    RecDateTime = Column()
    SMSDateTime = Column()
    Contents = Column(String(20))
    AlarmValue = Column(Float)
    Client = Column(String(50))
    ClientID = Column(Integer)
    File = Column(String(200))
    Meas_KeyNum = Column(Float)


class DailyReport(Base):
    __tablename__ = 'daily_report'
    ID = Column(Integer, primary_key=True)