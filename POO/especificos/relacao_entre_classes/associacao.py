# este conceito se refere a classes que possuem uma relação entre si 
# porem elas não depende uma da outra para poder existir elas podem existir 
# sozinhas sem haver a nescessidade de um existir

class Musico:
    def __init__(self, nome):
        self.nome = nome
        self.instrumento = None

class Violao:
    def __init__(self, marca):
        self.marca = marca

    def tocar(self):
        print('Tocando violão...')

class Piano:
    def __init__(self, marca):
        self.marca = marca
    
    def tocar(self):
        print('Tocando piano...')


musico = Musico('Astolfo')

musico.instrumento = Piano('Bosendorfer')
musico.instrumento.tocar()

musico.instrumento = Violao('Giannini')
musico.instrumento.tocar()