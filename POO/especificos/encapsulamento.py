# em outras linguagens a programação orientada a objeto nos temos os modificadores de acesso
# teremos metodos e atributos publicos (public), protegidos (protected), privado (private)
# o python não possui esses modificadores
# por convenção usamos um _ ou dois __
# exemplo: __dados
# com um _ se refere a um atributo que não é recomendado ser manipulado
# com dois __ se refere a um atributo que não é recomendado ser modificado FORTEMENTE!
# No caso da classe seguinte o atributo dados é se trata do "coração" da nossa classe
# então se ele for modificado tudo para de funcionar

class BaseDeDados:
    def __init__(self) -> None:
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def lista_cliente(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Astolfo')
bd.inserir_cliente(2, 'Frederico')
bd.inserir_cliente(3, 'Maria')
bd.apaga_cliente(3)
print(bd.dados)

