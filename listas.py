# CRUD com listas

# - Create
numeros = list()
numeros_b = []
# Adicionar valor ao final da lista
numeros.append(1)
numeros_b.append(2)

# Adicionar valor num lugar especifico da lista
numeros.insert(0, 10)

# - Read
print(numeros)
print(numeros_b[0])

# Update
numeros[1] = 35
numeros_c = numeros + numeros_b
numeros.extend(numeros_b)

# - Delete
# Remover valor do final ou um item especifico.
# Essa também função retorna o valor removido
numero_removido = numeros.pop()
# Remover um indice da lista usando del
del numeros[0]
# limpar toda lista
numeros.clear()
