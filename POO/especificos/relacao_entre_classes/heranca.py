class Mamifero:
    def __init__(self, genero):
        self.genero = genero
        
    def fazer_barulho(self):
        print('fazendo barulho')
    
    def amamentar(self):
        if self.genero == 'femea':
            print('amamentando')
        elif self.genero == 'macho':
            print('machos não amamentam.')

class Animal(Mamifero):
    def __init__(self, genero, nome):
        super().__init__(genero)
        self.nome = nome

class Gato(Animal):
    def __init__(self, genero, nome):
        super().__init__(genero, nome)
        

    def fazer_barulho(self):
        print('Miando')

