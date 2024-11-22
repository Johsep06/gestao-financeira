from flask import Flask

from database.database import get_db, set_db
# from . import app as src
from routes.home import home_route

app = Flask(__name__)

app.register_blueprint(home_route)


if __name__ == '__main__':
    app.run(debug=True)
    # db = []
    # try:
    #     db = get_db()
    #     src.nova_transacao(db, 
    #                        -1, 
    #                        'lanche', 
    #                        20, 
    #                        '2024-11-15', 
    #                        None)
    #     src.listar_transacoes(db)
    # except Exception as e:
    #     print('Erro na execussão', e)
    # finally:
    #     set_db(db)