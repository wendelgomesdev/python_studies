# essa é a relação mais forte entre as classes.
# neste caso se a classe principal for apaga 
# os objetos que ela carregava seram apagados com ela.

class Neuronio:
    def __init__(self): 
        pass

class Cerebro:
    def __init__(self):
        self.neunorios = []
    
    def construir_neuronio(self):
        neuronio = Neuronio()
        self.neunorios.append(neuronio)

    def __str__(self) -> str:
        return 'Quantidade de neuronios: '+ str(len(self.neunorios))

class Mamifero:
    def __init__(self, genero):
        self.genero = genero
        self.cerebro = Cerebro()
        
    def fazer_barulho(self):
        print('fazendo barulho')
    
    def amamentar(self):
        if self.genero == 'femea':
            print('amamentando')
        elif self.genero == 'macho':
            print('machos não amamentam.')

class Animal(Mamifero):
    def __init__(self, genero, nome):
        super().__init__(genero)
        self.nome = nome

class Gato(Animal):
    def __init__(self, genero, nome):
        super().__init__(genero, nome)
        

    def fazer_barulho(self):
        print('Miando')

alfonso = Gato('macho', 'Alfonso')

alfonso.cerebro.construir_neuronio()
alfonso.cerebro.construir_neuronio()
alfonso.cerebro.construir_neuronio()
alfonso.cerebro.construir_neuronio()

print(alfonso.cerebro)


class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoCompras:
    def __init__(self, cliente: Cliente, produtos: list):
        self.numero_pedido = '123'
        self.produtos = produtos
        self.cliente = cliente
    
    @property
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        
        return total

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)    

    def  fechar_carrinho(self):
        print(f'Fechando o pedito {self.numero_pedido}')
        print(f'Fechando o pedito {self.valor_carrinho}')
        print(f'Fechando o pedito {self.cliente.nome}')
        print('Obrigado pela compra!')


astolfo = Cliente('Astolfo', '123')

televisao = Produto('Televisão', 1000)
microondas = Produto('Microondas', 350)
guarda_roupas = Produto('Guarda-Roupas', 500)
notebook = Produto('NoteBook', 2000)

lista_produtos = [televisao, microondas, guarda_roupas]

carrinho_compras = CarrinhoCompras(astolfo, lista_produtos)

print(carrinho_compras.valor_carrinho)

carrinho_compras.adicionar_produto(notebook)

print(carrinho_compras.valor_carrinho)