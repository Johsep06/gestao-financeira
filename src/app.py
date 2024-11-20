from src.transacao import Transacao

def nova_transacao(db:list, tipo:int, categoria:str, valor:int, data:str, descricao:str, *args, **kwargs):
    """
    Cria uma nova transação

    \nparam db:list - lista de transações
    \nparam kwargs:dict - dicionario de dados<br/>
    <ul>
        <li>key tipo: int - se gasto ou ganho</li>
        <li>key categoria: str - categoria da transação</li>
        <li>key valor: float - valor da transação</li>
        <li>key data: str - data da transação 'yyyy-mm-dd</li>
        <li>key descricao: str - breve resumo da transação</li>
    </ul>
    """
    transacao = Transacao(
        tipo,
        categoria,
        valor,
        data,
        descricao
    )

    db.append(transacao)

def excluir_transacoes(db: list, *args):
    for i in args:
        if isinstance(i, int):
            del db[i]

def listar_transacoes(db:list):
    print(*db)