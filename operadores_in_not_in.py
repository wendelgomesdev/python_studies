frutas = ['Banana', 'Laranja', 'Goiaba', 'Maça', 'Manga']
fruta_digitada = input('Digite uma fruta: ')

if fruta_digitada in frutas:
    print(f'{fruta_digitada} está na lista!')

if fruta_digitada not in frutas:
    print(f'{fruta_digitada} não está na lista!')
