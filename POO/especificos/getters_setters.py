class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
    
    def deconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #Getter
    @property
    def nome(self):
        return self._nome
    
    #Setter
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome.upper()

    #Getter
    @property
    def preco(self):
        return self._preco 

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

televisao = Produto('Televisão', 2000)
notebook = Produto('Notebook', 2500)
celular = Produto('Celular', 900)
geladeira = Produto('Geladeira', 850)
microondas = Produto('Microondas', '500')

microondas.deconto(5)
televisao.deconto(10)
print(televisao.preco)
print(microondas.nome)