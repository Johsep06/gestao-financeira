INSERT = '''
INSERT INTO TRANSACAO (TIPO, CATEGORIA, VALOR, DATA, DESCRICAO) 
VALUES (:tipo, :categoria, :valor, :data, :descricao)
'''

DELETE = '''
DELETE 
FROM TRANSACAO 
WHERE ID = :id
'''