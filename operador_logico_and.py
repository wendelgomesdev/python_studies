entrada = input('[E]ntrar [S]air: ')
senha_permitida = 123456
senha_digitada = input('Senha: ')

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrando...')
else:
    print('Saindo...')