from core.db.pg.base import Session


# Зависимость для получения сессии БД
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()