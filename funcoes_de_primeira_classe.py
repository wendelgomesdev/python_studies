def saudacao(msg):
    return msg

saudacao_2 = saudacao

print(saudacao_2('teste'))

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Testando isso!')

print(v)