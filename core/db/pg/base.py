from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL для подключения к PostgreSQL
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# Создаём движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаём фабрику сессий для взаимодействия с БД
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
