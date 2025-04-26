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
                cursor.execute(create.FATURA_CARTAO)
                connection.commit()
                # cursor.execute(create.TRASACOES_POR_ANO)
                # connection.commit()
                # cursor.execute(create.TRASACOES_POR_MES)
                # connection.commit()
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
                connection.commit()
                print('Transação inserida com sucesso.')
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

def get_fatura():
        valor_fatura = None
        
        try:
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                cursor.execute(read.FATURA)
                valor_fatura = cursor.fetchall()[0]
        except Exception as e:
                print('Erro ao acessar o db', str(e))
        finally:
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')
                return valor_fatura

def get_saldo():
        saldo = None
        
        try:
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                cursor.execute(read.SALDO)
                saldo = cursor.fetchall()[0]
        except Exception as e:
                print('Erro ao acessar o db', str(e))
        finally:
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')
                return saldo

def get_despesas_do_mes(mes:int, ano:int):
        despesas = None
        
        try:
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                param = {'mes':f'{mes:0>2}', 'ano':f'{ano}'}
                cursor.execute(read.DESPESAS_DO_MES, param)
                despesas = cursor.fetchall()
        except Exception as e:
                print('Erro ao acessar o db', str(e))
        finally:
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')
                return despesas

def get_receitas_do_mes(mes:int, ano:int):
        despesas = None
        
        try:
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                param = {'mes':f'{mes:0>2}', 'ano':f'{ano}'}
                cursor.execute(read.RECEITA_DO_MES, param)
                despesas = cursor.fetchall()
        except Exception as e:
                print('Erro ao acessar o db', str(e))
        finally:
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')
                return despesas

def get_todas_transacoes():
        transacoes = None
        
        try:
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()
                cursor.execute(read.TODAS_AS_TRANSACOES)
                transacoes = cursor.fetchall()
        except Exception as e: 
                print('Erro ao acessar o db', str(e))
        finally:
                cursor.close()
                connection.close()
                print('Conexão com o db encerrada.')
                return transacoes