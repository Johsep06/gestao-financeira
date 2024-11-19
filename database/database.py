from pathlib import Path
from database.json.banco_json import salvar_em_json, ler_de_json

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.json'
DB_FILE = ROOT_DIR / DB_NAME

def get_db() -> list[dict]:
    try:
       return ler_de_json(DB_FILE)
    except Exception as e:
        return []

def set_db():
    try:
        salvar_em_json(DB_FILE)
    except Exception as e:
        print('Erro:' + str(e))