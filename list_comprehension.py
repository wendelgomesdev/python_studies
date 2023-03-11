# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# Dobrar o valor dos produtos em uma lista
lista_precos = [25, 30, 40, 45, 80, 100, 264]

nova_lista_precos = [preco * 2 for preco in lista_precos]


# Dar desconto em produtos em um diconario
produtos = [ 
        {'nome': 'p1', 'preco': 20, },
        {'nome': 'p2', 'preco': 10, },
        {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

# filtrar lista

lista = [n for n in range(10), if n < 5]
