# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

# Manipulando chaves e valores em dicionarios

#Criar/Alterar chaves
pessoa['pais_origem'] = 'Brasil'

# Acessar
print(pessoa['pais_origem'])

# Criando dinamicamente
chave = 'livro_favorito'

pessoa[chave] = 'Os tres Porquinhos'

print(pessoa)

# Tentar obter uma chave
if pessoa.get('estado_civil') is None:
    print('Não existe!')

# Metodos uteis

# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = { 'nome': 'Itagiane', 'idade': 22}

# Obter chaves e valores do dicionario
a = tuple(pessoa.items())

# Obter valores das chaves de um dicionario
b = list(pessoa.values())

print(a)
print(b)

# Deletar uma chave especifica
nome = pessoa.pop('nome')

print(nome)


# Deletar a ultima chave do dicionario
ultima_chave = pessoa.popitem()

print(ultima_chave)

# Editar dicioanrio
pessoa.update(
        {
        'nome': 'João',
        'idade': 45
        }
)