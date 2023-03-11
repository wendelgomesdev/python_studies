import time

class Impressora:
    modelo = 'Epson'

    def __init__(self, numero_folha):
        self.numero_folha = numero_folha
    
    def imprimir_folha(self):
        print('imprimindo folha')
        time.sleep(1)
        print('folha impressa!')
        self.numero_folha -= 1
    
    @classmethod
    def mostrar_modelo(cls):
        print(cls.modelo)
    
    def mostrar_modelo_instancia(self):
        print(self.modelo)

impressora = Impressora(10)

impressora.mostrar_modelo()
impressora.mostrar_modelo_instancia()