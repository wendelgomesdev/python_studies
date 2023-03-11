# metodos estaticos é declarado dentro de uma classe, 
# porem ele não tem o escopo da classe, somento o proprio

# Geralmente usamos métodos estáticos para criar funções utilitárias.
# Funciona como uma função criada fora da class, mas por uma questao de 
# organização precisa estar dentro da class.

class Impressora:
    modelo = 'Epson'
    
    @staticmethod
    def ligar_para_suporte():
        print('ligando para suporte...')

    @classmethod
    def problema_impressora(cls):
        cls.ligar_para_suporte()

Impressora.ligar_para_suporte()

Impressora.problema_impressora()