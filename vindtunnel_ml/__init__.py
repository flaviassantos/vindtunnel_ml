import importlib_resources as _resources
from configparser import ConfigParser as _ConfigParser

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__version__ = "0.0.1"

# Read database parameters from config file
_cfg = _ConfigParser()
with _resources.path("vindtunnel_ml", "config.cfg") as _path:
    _cfg.read(str(_path))

USER = _cfg.get("db", "_USER")
PASSWORD = _cfg.get("db", "_PASSWORD")
HOSTNAME = _cfg.get("db", "_HOSTNAME")
PORT = _cfg.get("db", "_PORT")
DATABASE = _cfg.get("db", "_DATABASE")

engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}',
                       echo=True)
metadata = MetaData(bind=engine, schema=DATABASE)
Base = declarative_base(metadata=metadata)

Session = sessionmaker(bind=engine)