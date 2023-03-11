import decimal

# Para ter mais precição nos resultados 
# de operações com numeros de ponto flutuante
numero_1 = decimal.Decimal('0.33214') / decimal.Decimal('0.987413')
numero_2 = decimal.Decimal(0.23547)
resultado = numero_1 + numero_2

print(resultado)