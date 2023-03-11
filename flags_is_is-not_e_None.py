# Diferença entre "is" e "=="
# "is" verifica a igualdade
# "==" verifica a identidade

# Caso duas variaveis sejam tradadas como sendo o mesmo objeto, por terem os mesmos valores, 
# isso se dá devido a uma particularidade do python que faz com que duas variveis, com valores iguais, 
# aponte para o mesmo local na memoria para economizar espaço na memoria.

numero1 = 123
numero2 = 123

print('Checando igualdade de valores: ', numero1 == numero2)
print('Checando se são os mesmos objetos na memoria: ', numero1 is numero2)
print(id(numero1), id(numero2))
print('   ')

numero1 = [123, 456]
numero2 = [123, 456]

print('Checando igualdade de valores: ', numero1 == numero2)
print('Checando se são os mesmos objetos na memoria: ', numero1 is numero2)
print(id(numero1), id(numero2))
print('   ')


# uma variavel em python nunca pode ser criada vazia
# sempre um valor deve ser atribuido a ela. 
# Este valor pode ser o None

# Se duas variveis com None forem testada com "is" sempre será True
# pois sempre há um None em python. None sempre será o mesmo objeto.

print(id(None))
teste = None
print(id(teste))

# "None" deve ser sempre verificado com "is" ao inves de "=="

if teste is None:
    print('É None')