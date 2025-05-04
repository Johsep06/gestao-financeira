from src.transacao import Transacao
from database import database

def transacoes_filtradas_por_data_e_tipo(ano:int, mes:int, tipo:int) -> list[Transacao]:
    '''
    Filtra as transações por ano, mês e tipo (receita ou despesa).

    :param ano: Ano para o qual filtrar as transações.
    :param mes: Mês para o qual filtrar as transações.
    :param tipo: Tipo de transação (1 para receita, -1 para despesa).
    :return: Lista de transações filtradas.
    '''
    
    transacoes = database.get_todas_transacoes()
    transacoes_filtradas_por_mes = list(filter(lambda x: f'{ano}-{mes:0>2}' in x['data'], transacoes))
    transacoes_filtradas = list(filter(lambda x: x['tipo'] == tipo, transacoes_filtradas_por_mes))
    
    return transacoes_filtradas

def historico_despesas_do_mes(ano:int, mes:int) -> dict[str, float]:
    '''
    retorna o historico de despesas para um determinado mês e ano

    :param ano: Ano para o qual buscar as despesas.
    :param mes: Mês para o qual buscar as despesas.
    :return: Histórico de despesas para o mês e ano especificados.
    '''
    transacoes = transacoes_filtradas_por_data_e_tipo(ano, mes, -1)
    
    datas = [x['data'] for x in transacoes]
    datas = list(set(datas))
    datas.sort()
    historico_despesas_do_mes = { data:0 for data in datas }
    for transacao in transacoes:
        data = transacao['data']
        valor = transacao['valor']
        historico_despesas_do_mes[data] += round(valor, 2)
    
    return historico_despesas_do_mes

def percentual_de_despesas_do_mes(ano:int, mes:int) -> dict[str, float]:
    '''
    Calcula a média de despesas para um determinado mês e ano

    Calcula a média de despesas para um determinado mês e ano.
    
    :param ano: Ano para o qual calcular a média de despesas.
    :param mes: Mês para o qual calcular a média de despesas.
    :return: Média de despesas para o mês e ano especificados.
    '''
    transacoes = transacoes_filtradas_por_data_e_tipo(ano, mes, -1)
    
    categorias = list(set(map(lambda x: x['categoria'], transacoes)))

    total_despesas = sum(map(lambda x: x['valor'], transacoes))
    percentual_de_despesas = {}

    for categoria in categorias:
        transacoes_de_categoria = list(filter(lambda x: x['categoria'] == categoria, transacoes))
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
    transacoes = transacoes_filtradas_por_data_e_tipo(ano, mes, 1)
    
    categorias = list(set(map(lambda x: x['categoria'], transacoes)))
    total_receitas = sum(map(lambda x: x['valor'], transacoes))
    percentual_de_receitas = {}
    
    for categoria in categorias:
        transacoes_de_categoria = list(filter(lambda x: x['categoria'] == categoria, transacoes))
        percentual_de_receitas[categoria] = sum(map(lambda x: x['valor'], transacoes_de_categoria)) / total_receitas * 100
        percentual_de_receitas[categoria] = round(percentual_de_receitas[categoria], 2)
        
    return percentual_de_receitas
