from src.transacao import Transacao
from database import database

def percentual_de_despesas_do_mes(ano:int, mes:int) -> dict[str, float]:
    '''
    Calcula a média de despesas para um determinado mês e ano

    Calcula a média de despesas para um determinado mês e ano.
    
    :param ano: Ano para o qual calcular a média de despesas.
    :param mes: Mês para o qual calcular a média de despesas.
    :return: Média de despesas para o mês e ano especificados.
    '''
    transacoes = database.get_todas_transacoes()
    transacoes_filtradas_por_mes = list(filter(lambda x: f'{ano}-{mes:0>2}' in x['data'], transacoes))
    transacoes_filtradas = list(filter(lambda x: x['tipo'] == -1, transacoes_filtradas_por_mes))
    
    categorias = list(set(map(lambda x: x['categoria'], transacoes_filtradas)))

    total_despesas = sum(map(lambda x: x['valor'], transacoes_filtradas))
    percentual_de_despesas = {}

    for categoria in categorias:
        transacoes_de_categoria = list(filter(lambda x: x['categoria'] == categoria, transacoes_filtradas))
        percentual_de_despesas[categoria] = sum(map(lambda x: x['valor'], transacoes_de_categoria)) / total_despesas * 100
        percentual_de_despesas[categoria] = round(percentual_de_despesas[categoria], 2)

    return percentual_de_despesas

def percentual_de_receita_do_mes(ano:int, mes:int) -> dict[str, float]:
    '''
    Calcula a média de receita para um determinado mês e ano

    Calcula a média de receita para um determinado mês e ano.
    
    :param ano: Ano para o qual calcular a média de receita.
    :param mes: Mês para o qual calcular a média de receita.
    :return: Média de receita para o mês e ano especificados.
    '''
    transacoes = database.get_todas_transacoes()
    transacoes_filtradas_por_mes = list(filter(lambda x: f'{ano}-{mes:0>2}' in x['data'], transacoes))
    transacoes_filtradas = list(filter(lambda x: x['tipo'] == 1, transacoes_filtradas_por_mes))
    
    categorias = list(set(map(lambda x: x['categoria'], transacoes_filtradas)))
    total_receitas = sum(map(lambda x: x['valor'], transacoes_filtradas))
    percentual_de_receitas = {}
    
    for categoria in categorias:
        transacoes_de_categoria = list(filter(lambda x: x['categoria'] == categoria, transacoes_filtradas))
        percentual_de_receitas[categoria] = sum(map(lambda x: x['valor'], transacoes_de_categoria)) / total_receitas * 100
        percentual_de_receitas[categoria] = round(percentual_de_receitas[categoria], 2)
        
    return percentual_de_receitas