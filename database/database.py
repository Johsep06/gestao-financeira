import sqlite3
from pathlib import Path

from database.scripts import basic, read, update, create

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

def init_db():
        try: 
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                cursor.execute(create.TABLE)
                connection.commit()
                cursor.execute(create.TRASACOES_POR_ANO)
                connection.commit()
                cursor.execute(create.TRASACOES_POR_MES)
                connection.commit()
        except Exception as e:
                print('Erro ao Criar o db', str(e))
        finally: 
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')
        

def add(trasacao:dict):
        try: 
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                cursor.execute(basic.INSERT, trasacao)
        except Exception as e:
                print('Erro ao acessar o db', str(e))
        finally: 
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')

def delete(*ids):
        try: 
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                for id in ids:
                        param = {'id':id}
                        cursor.execute(basic.DELETE, param)
                        connection.commit()
        except Exception as e:
                print('Erro ao acessar o db', str(e))
        finally: 
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')


def get_by_id(id:int):
        transacao = None
        
        try: 
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                param = {'id':id}
                cursor.execute(read.BY_ID, param)
                transacao = cursor.fetchall()
        except Exception as e:
                print('Erro ao acessar o db', str(e))
        finally:
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')
                return transacao


