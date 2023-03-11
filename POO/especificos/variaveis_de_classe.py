# é posivel criar variaveis que pertence as classes 
# quando alteramos seus valores, alteramos para todas 
# as classes e não somente para as instacia separadamente

class A:
    variavel = 123

instacia_um = A()
instacia_dois = A()

A.variavel = 456

print(instacia_um.variavel)
print(instacia_dois.variavel)

# E no caso de alterarmos esta variavel na instacia?
instacia_um.variavel = 789
# a variavel parece ter sido alterada somente 
# na instacia que recebeu o novo valor 
# mas na verdade quando solicitamos uma variavel de uma instacia
# primeiramente o interpretador do python procura na instancia 
# caso não encontre ele procurar na classe.
print(instacia_um.variavel)
print(instacia_dois.variavel)