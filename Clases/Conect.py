from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


DB_URL = 'postgresql://postgres:root@localhost/db_transferencia'
engine = create_engine(DB_URL)
Base = declarative_base()
 