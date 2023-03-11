# For

frutas = ['Banana','Goiaba','Manga','Laranja','Mexirica']

# Percorrer toda lista
for a in frutas:
	print(a)
	
print('-----------')
print('   ')

# Percorrer lista, determinando comeco e fim
for  b in range(0,3,):
	print(frutas[b])

print('-----------')
print('   ')

# Percorrer lista e pegar seu indice
for ind, c in enumerate(frutas):
	print(f'{ind} {c}')

print('-----------')
print('   ')

# While

# Percorrer lista usando while

contador = 0
while contador != len(frutas):
	print(frutas[contador])
	contador += 1