valor = input(' Escreva algo: ')

strin = str(valor)

#Verificar se é um número
if valor.isnumeric(): intei = int(valor)
if valor.isnumeric(): flut = float(valor)
bole = bool(valor)

print(' String: ', strin)
if valor.isnumeric(): print(' Inteiro: ', intei)
if valor.isnumeric(): print(' Real: ', flut)
print(' Boleano: ', bole)