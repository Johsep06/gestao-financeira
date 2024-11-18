class Transacao:
    def __init__(self, tipo:int, categoria:str, valor:float, data:tuple[int], descricao:str=None):
        self.tipo = tipo
        self._categoria = categoria
        self._valor = valor
        self._descricao = descricao
        self._data = data
    
    @property
    def tipo(self) -> int:
        return self._tipo 
    @tipo.setter
    def tipo(self, tipo:int):
        self._tipo = tipo / abs(tipo)
    
    @property
    def categoria(self) -> str:
        return self._categoria
    @categoria.setter
    def categoria(self, categoria:str):
        self._categoria = categoria

    @property
    def valor(self) -> int:
        return self._valor
    @valor.setter
    def valor(self, valor:int):
        self._valor = valor

    @property
    def descricao(self) -> str | None:
        return self._descricao
    @descricao.setter
    def descricao(self, descricao:str):
        self._descricao = descricao

    @property
    def data(self) -> tuple[int]:
        return self._data
    @data.setter
    def data(self, data:tuple[int]):
        self._data = data
    
    def __str__(self):
        s = ''

        s = f'''
            \rCategoria: {self._categoria}.
            \rValor: {(self._valor*self.tipo):.2f}
            \rData: {self._data[0]:0>2}/{self._data[1]}.
            \rDescrição: {self._descricao}.
        '''

        return s
    
    def to_dict(self) -> dict:
        d = {}
        d.setdefault('tipo', self._tipo)
        d.setdefault('categoria', self._categoria)
        d.setdefault('valor', self._valor)
        d.setdefault('data', self._data)
        d.setdefault('descricao', self._descricao)

        return d

if __name__ == '__main__':
    teste:list[Transacao] = []
    teste.append(Transacao(-12, 'conta', 32.00, (10,24)))
    teste.append(Transacao(1, 'presente', 62.00, (9,24)))
    teste.append(Transacao(-1, 'passagem', 23.00, (8,24)))
    teste.append(Transacao(1, 'lanche', 72.00, (11,24)))
    # print(*teste)

    lista = [t.to_dict() for t in teste]

    # print(*lista, sep='\n')