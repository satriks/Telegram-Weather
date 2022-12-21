from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import User, Base, WeatherReports

from setting import database_config

engine = create_engine(database_config.url, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_user(tg_id):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    if user is None:
        new_user = User(tg_id=tg_id)
        session.add(new_user)
        session.commit()

def set_user_city(tg_id, city):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    user.city = city
    session.commit()

def create_report(tg_id, temp, feels_like, wind_speed, pressure_mm, city):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    new_report = WeatherReports(temp=temp, feels_like=feels_like, wind_speed=wind_speed, pressure_mm=pressure_mm, city=city, owner=user.user_id)
    session.add(new_report)
    session.commit()

def get_user_city(tg_id):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    if user.city.strip() == '':
        user.city = None
    return user.city

def get_reports(tg_id):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    report = user.reports
    return  report

def delete_user_report(report_id):
    session = Session()
    report = session.get(WeatherReports, report_id)
    session.delete(report)
    session.commit()

def get_all_users():
    session = Session()
    users = session.query(User).all()
    return users