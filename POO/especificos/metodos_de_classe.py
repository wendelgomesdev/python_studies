from datetime import date

class Impressora():
    @classmethod
    def imprimir_folha(cls):
        print('folha impressa')
    
    @classmethod
    def imprimir_livro(cls, paginas: int):
        for i in range(paginas):
            cls.imprimir_folha()

# é possivel usar os metodos de classes e chama-los sem instaciar a classe
Impressora.imprimir_folha()
print('================')
Impressora.imprimir_livro(3)
print('================')

# também é possilvel chamar um metodo de classe por meio de uma instacia
impressora_epson = Impressora()

impressora_epson.imprimir_folha()
print('================')
impressora_epson.imprimir_livro(5)

# Geralmente usamos o método de classe para criar métodos de fábrica. 
# Métodos de fábrica retornam objetos de classe (semelhante a um construtor, __init__) 
# para diferentes casos de uso.

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_por_ano_nascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    @staticmethod
    def verificar_maior_idade(idade):
        return idade > 18

p1 = Pessoa('Astolfo', 25)

p2 = Pessoa.criar_por_ano_nascimento('Frederico', 2010)

print(Pessoa.verificar_maior_idade(p2.idade))