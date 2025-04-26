from flask import Blueprint, render_template, request, jsonify
from src.transacao import Transacao
from database import database

forms_route = Blueprint('forms', __name__)

@forms_route.route('/')
def forms():
    return render_template('tela-nova-transacao.html')

@forms_route.route('/nova-transacao', methods=['POST'])
def nova_transacao():
    dados = request.get_json()

    nova_transacao = Transacao(
        dados['tipo'],
        dados['categoria'],
        dados['valor'],
        dados['data'],
        dados['descricao'],
    )
    
    database.add(nova_transacao.to_dict())
    return jsonify(
        {'ok':True}
    )