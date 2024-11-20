from database.database import get_db, set_db
from src import app

if __name__ == '__main__':
    db = []
    try:
        db = get_db()
        app.nova_transacao(db, 
                           -1, 
                           'transporte', 
                           26, 
                           '2024-11-15', 
                           None)
        app.listar_transacoes(db)
    except Exception as e:
        print('Erro na execussão', e)
    finally:
        set_db(db)