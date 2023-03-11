numero_str = input('Vou dobrar o numero que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except Exception:
    print('Você não digitou um numero.')

# Com finally
try:
    print('Abrir arquivo')
    8/0
except ZeroDivisionError:
    print('Dividiu por zero')
finally:
    print('Fechar arquivo arquivo')

# Com else 
try:
    print('Tentar executar')
    8/1
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('tudo ok ao executar')