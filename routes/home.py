from flask import Blueprint, render_template, jsonify
import datetime

from database import database

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    hoje = datetime.datetime.now()
    
    despesas_do_mes = database.get_despesas_do_mes(hoje.month, hoje.year)
    receitas_do_mes = database.get_receitas_do_mes(hoje.month, hoje.year)
    
    if despesas_do_mes:
        # despesas_do_mes = sum(despesas_do_mes, key=lambda x: x['valor'])
        valor = 0.0
        for despesa in despesas_do_mes:
            valor += despesa['valor']
        despesas_do_mes = valor
    else:
        despesas_do_mes = 0.0
        
    if receitas_do_mes:
        # receitas_do_mes = sum(receitas_do_mes, key=lambda x: x['valor'])
        valor = 0.0
        for receita in receitas_do_mes:
            valor += receita['valor']
        receitas_do_mes = valor
    else:
        receitas_do_mes = 0.0
        
    fatura = database.get_fatura()[0]
    saldo = database.get_saldo()[0]
    return render_template(
        'index.html',
        fatura=f'{fatura:,.2f}', 
        saldo=f'{saldo:,.2f}',
        despesas_do_mes=f'{despesas_do_mes:,.2f}',
        receitas_do_mes=f'{receitas_do_mes:,.2f}'
    )