# - Fatiamento
texto = 'Astolfo Ribeiro Silva'
#[posicao inicial : posicao final : intervalo]
#deixando em branco sera interpreta que a posicao de inicio sera a primeira, a final sera a ultima (caso haja algun valor para o ultimo valor, ele pegara o penultimo valor antes do ultimo selecionado) e o intervalo sera de 1 em 1

print(' ', texto[::])

print(' ',texto[1:17:2])

# - Analise

#Contar quantos caracteres há na string
print(' ',len(texto))

#Contar quantidade 
#de um caracteres especifico
print(' ', texto.count('o'))

#Contar quantidade 
#de caracteres especificos
#em posicoes selecionadas
print(' ', texto.count('o',0,8))

#Mostra onde comecou uma ocorrencia
print(' ', texto.find('Rib'))

if 'Ribeiro' in texto:
	print(' O sobrenome desse cara tem Ribeiro')

# - Transformação

#Substituir um valor encontrado
#nao diretamente na string
texto.replace('Ribeiro', 'Silva')

#Transformar tudo em maiusculas
texto.upper()

# Transformar tudo em minusculas
texto.lower()

# Transformar primeiro 
#caractere em maiusculo
texto.capitalize()

# Transforma primeira letra das palavras
# em maiuscula
texto.title()

#Remover espaços do inicio e do fim de uma string

textocomespaco = "   teste testando "
print(textocomespaco.strip())


# Remover espaços do lado direito da string
print(textocomespaco.rstrip())

# Remover espaços do lado esquerdo da string
print(textocomespaco.lstrip())

# - Dividir 

# Dividir string em partes separando por espaços e montando uma lista
textoparadividir = 'Wendel Gomes Silva'
textoparadividir.split()

# - Junção

print(','.join(textoparadividir))