from database.database import get_db, set_db
from src import app

if __name__ == '__main__':
    db = []
    try:
        db = get_db()
    except:
        set_db(db)