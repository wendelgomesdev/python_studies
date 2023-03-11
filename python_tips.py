# Concatenar strings

nome = 'Wendel'
sobrenome = 'Gomes'

nome_sobrenome = nome + ' ' + sobrenome

# Não é possivel concatenar uma string e um inteiro
# Somando inteiros
num1 = 1
num2 = 6

resultado = num1 + num2

# ==========================================================

# Built-in types

# criando uma lista
lista_frutas = ['banana', 'maça', 'goiaba']

# acrescentando elementos na lista
lista_frutas.append('melancia')

# removendo elementos em uma lista
lista_frutas.remove('banana')

# acessando primeiro elemento da lista
lista_frutas[0]

# acessando o ultimo elemento da lista
lista_frutas[-1]

# ==========================================================

# criando uma tupla
tupla = (1, 2, 3, 4)

# Procura por vezes que um certo elemento aparece na tupla
tupla.count(1)

# Verifica em qual posicao um certo elemento se encontra
tupla.index(4)

# ==========================================================

# criando dicionario
dicionario = {'nome': 'Astolfo', 'idade': 35}

# adiocnando chaves em dicionarios
dicionario['cidade'] = 'São Paulo'

# removendo chaves de um dicionario
del dicionario['cidade']

# o mesmo serve para uma variavel
teste = 123

del teste

# ==========================================================

# estruturas condicionais
# ordem de presedencia usando ()
if (2+2) * 3 == 12:
    print('correto')

# alguns tipos em python são entendidos como True ou False

# uma string com conteudo é interpretada como True
teste_string = 'string'

if teste_string:
    print(teste_string)


# uma lista com conteudo é interpretada como True
teste_lista = ['teste1', 'teste2']

if teste_lista:
    print(teste_lista)

teste_lista2 = []

# Vazia como False
if teste_lista2:
    print(teste_lista2)

# ==========================================================

# formatando uma string
nome = 'Wendel Gomes Silva'

# formatar string com somente os 6 primeiros caracteres em print
print(f'Nome: {nome:.6}')


dinheiro = 5.7
# formatar valor float com formato moeda
print(f'dinheiro: R$ {dinheiro:.2f}')


# ==========================================================
# PEP8
# Normas de formatação do codigo

# para instalar 
# pip install flake8

# para verificar codigo
#flake8 nome_do_arquivo.py
