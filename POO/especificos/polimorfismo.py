# polimorfismo é a capacidade de uma classe abstrata definir um corportamento generico e nas extensões dessa o mesmo comprtamento se torna mais especifico 
class Mamifero:
    def emitir_som(self):
        pass

class Cachorro(Mamifero):
    def emitir_som(self):
        print('Au, Au, Au')

class Gato(Mamifero):
    def emitir_som(self):
        print('Miau')


astolfo = Cachorro()
alfonso = Gato()

astolfo.emitir_som()
alfonso.emitir_som()