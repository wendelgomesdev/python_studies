from __future__ import annotations
# agregacao se trate de objetos que existem separadamente porem eles depende uns dos outros
# a classe carrinho de compras pode existir sem a classe produto
# porem toda sua estrutura será inutil 
# porque sua funcionalidade depende de produtos

class CarrinhoCompras:
    def __init__(self):
        self.produtos : Produto = []

    def adicionar_produto(self, produto : Produto):
        self.produtos.append(produto)
    
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho_compras = CarrinhoCompras()

carrinho_compras.adicionar_produto(Produto('Televisão', 950))
carrinho_compras.adicionar_produto(Produto('Celular', 600))
carrinho_compras.adicionar_produto(Produto('Notebook', 2000))

carrinho_compras.lista_produto()
print('Total:', carrinho_compras.soma_total())



    