from pathlib import Path
from database.json.banco_json import salvar_em_json, ler_de_json
from src.transacao import Transacao

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.json'
DB_FILE = ROOT_DIR / DB_NAME

def get_db() -> list[Transacao]:
    try:
       data = ler_de_json(DB_FILE)
       db = []

       for dado in data:
            db.append(Transacao(**dado))
       return db 
    except Exception as e:
        print(e)
        return []

def set_db(db:list):
    dados = []
    for l in db:
        dados.append(l.to_dict())
    try:
        salvar_em_json(dados, DB_FILE)
    except Exception as e:
        print('Erro:' + str(e))