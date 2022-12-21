from sqlalchemy import Column, ForeignKey , Integer, String, DateTime ,create_engine, select, BigInteger
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import psycopg2

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    city = Column(String(40))
    connection_date = Column(DateTime , default=datetime.now())
    reports = relationship('WeatherReports', backref='report', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return self.tg_id

class  WeatherReports(Base):
    __tablename__ = 'WeatherReports'
    wr_id = Column(Integer,primary_key=True)
    owner = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    date = Column(DateTime, default=datetime.now())
    temp = Column(Integer, nullable=False)
    feels_like = Column(Integer, nullable=False)
    wind_speed = Column(Integer, nullable=False)
    pressure_mm = Column(Integer, nullable=False)
    city = Column(String(40), nullable=False)

    def __repr__(self):
        return self.city


if __name__ == '__main__':
    engine = create_engine('postgresql://postgres:123st321@localhost:5432/botwether', echo=False)
    Base.metadata.create_all(engine)
