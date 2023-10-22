import os
from datetime import datetime as dt
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Создание сессии
POSTGRES_DB = os.environ.get('POSTGRES_DB', default='postgres')
POSTGRES_USER = os.environ.get('POSTGRES_USER', default='postgres')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default='0.0.0.0')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', default='5432')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default='postgres')

SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

#print(POSTGRES_DB, POSTGRES_USER, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_PASSWORD)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Подключение базы (с автоматической генерацией моделей)
class Base(DeclarativeBase):
    pass


class Question(Base):
    """Таблица question"""
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
    saved_at = Column(DateTime, default=dt.now())


Base.metadata.create_all(bind=engine)
