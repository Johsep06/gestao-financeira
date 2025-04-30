from flask import Blueprint, jsonify

from src import app
from database import database

data_route = Blueprint('data', __name__)

@data_route.route('/')
def data():
    return jsonify(database.get_todas_transacoes())

@data_route.route('/percental/despesas/<int:ano>-<int:mes>')
def percentual_de_despesas(ano:int, mes:int):
    """
    Retorna o percentual de despesas e receitas para um determinado mês e ano.
    
    :param ano: Ano para o qual calcular o percentual.
    :param mes: Mês para o qual calcular o percentual.
    :return: Percentual de despesas e receitas para o mês e ano especificados.
    """
    
    return jsonify(app.percentual_de_despesas_do_mes(ano, mes))

@data_route.route('/percental/receitas/<int:ano>-<int:mes>')
def percentual_de_receitas(ano:int, mes:int):
    """
    Retorna o percentual de receitas para um determinado mês e ano.
    
    :param ano: Ano para o qual calcular o percentual.
    :param mes: Mês para o qual calcular o percentual.
    :return: Percentual de receitas para o mês e ano especificados.
    """
    
    return jsonify(app.percentual_de_receita_do_mes(ano, mes))