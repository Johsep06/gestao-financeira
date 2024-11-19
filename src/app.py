from src.transacao import Transacao

def nova_transacao(db:list, **kwargs):
    transacao = Transacao(
        kwargs['tipo'], 
        kwargs['categoria'],
        kwargs['valor'],
        kwargs['data'],
        kwargs['descricao'],
    )

    db.append(transacao)

def excluir_transacoes(db: list, *args):
    for i in args:
        if isinstance(i, int):
            del db[i]
