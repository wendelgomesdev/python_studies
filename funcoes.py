titulos = ['Funções em Python','Funções sem parametros', 'Funções com parametros']

# Sem parametros
def linha():
	print('--------------------------------------')
	
for a in titulos:
	linha()
	print(a)
	linha()
	
	
# Com parametros
def linha_dinamica(tamanho):
	print('-'*tamanho)
	
for indice, b in enumerate(titulos):
	linha_dinamica(len(titulos[indice]))
	print(b)
	linha_dinamica(len(titulos[indice]))
	
# Parametros com valores padroes
def funcao_valores_padrao(numero_2, numero=None):
	if numero is not None:
		print(numero + numero_2)

# Empacotar parametros
def criar_titulos(*titulos):
	for c in titulos:
		print(c)

# Enviar uma iteravel desempacotado como argumento
lista = ['teste', 'testando', 'terereste']
criar_titulos(*lista)

criar_titulos('teste1','teste2','teste3','teste4')

# Função com lista 
def titulos_com_lista(lista):
	for d in lista:
		print(d)
	
titulos_com_lista(['teste','testando2'])

#Parametro opcional
def usuario(idade, sexo, nome='desconhecido'):
	print(nome)
	print(idade)
	print(sexo)
	
usuario(idade=25, sexo='M')

# Escopo de variavel 
variavel1 = 1

# Assim vai funcionar normalmente
def teste():
	print(variavel1)

teste()

# Escopo de variavel 
variavel2 = 1

# Assim sera usada a variavel de dentro da função
def teste2():
	variavel2 = 2
	print(variavel2)

teste2()

# Escopo de variavel 
variavel3 = 1

# Para usar a variavel fora da fução, é preciso utilizar o global
def teste3():
	global variavel3
	variavel3 = 2
	print(variavel3)

teste3()

# Retorno de valores

def retornar_soma(a,b):
	return a + b

print(retornar_soma(4,5))
