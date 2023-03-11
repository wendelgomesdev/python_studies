from functools import partial
import time
import threading
from elementos_janela import Janela, Quadro, Botao, CaixaTexto

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0 
    
    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node
        
        self._size += 1

    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        raise IndexError('The Queue is empty')

    def peek(self):
        if self._size > 0:
            return self.first.data
        raise IndexError('The Queue is empty')

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ''
            pointer = self.first
            while(pointer):
                r += str(pointer.data) + ' '
                pointer = pointer.next
            return r
        else:
            return 'Empty Queue'

    def __str__(self):
        return self.__repr__()

""" 
class ProcessQueue:
    def __init__(self):
        self.processes = Queue()

    def insert_process(self, process):
        self.processes.push(elem=process)

        if len(self.processes) == 1:
            self.start_process()
    
    def call_next(self):
        self.start_process()

    def start_process(self):
        self.processes.peek()()

        self.processes.pop()

        if len(self.processes) > 0:
            self.call_next()

a = ProcessQueue()

a.insert_process(funcao)
a.insert_process(funcao)
a.insert_process(funcao)
a.insert_process(funcao)
a.insert_process(funcao)
a.insert_process(funcao)
 """

class App(Janela):
    def __init__(self):
        super().__init__('Counter')

        self.main_frame = Quadro(self, 0, 0, 1, 1)

        self.last_number = CaixaTexto(self.main_frame, eixo_x=0.25, eixo_y=0.25, largura=0.5, altura=0.1)
        
        comando_botao_iniciar = lambda: threading.Thread(target=self.insert_queue).start()
        self.button_start = Botao(self, texto='Start counting ->', comando=comando_botao_iniciar, eixo_x=0.25, eixo_y=0.50, largura=0.5, altura=0.1)
        
        self.queue_process = Queue()

    def insert_queue(self):
        last_number = int(self.last_number.get()) + 1
        self.funcao_iniciar_contagem = partial(self.start_counting, last_number)
        self.queue_process.push(elem=self.funcao_iniciar_contagem)
        
        if len(self.queue_process) == 1:
            self.call_next()

    def call_next(self):
        self.queue_process.peek()()
            
    def start_counting(self, number):

        print(' ')
        print('=====================')
        print(' ')
        print('Counting...')
        for i in range(number):
            print(i)
            time.sleep(1)

        print('OK!')
        print(' ')
        print('=====================')
        print(' ')
        
        self.queue_process.pop()

        if len(self.queue_process) > 0:
            self.call_next()
            

if __name__ == "__main__":
    app = App()
    app.mainloop()

""" 
from PIL import Image

class Wimp:
        
    def proporcional_crop(imagem, proporcao):
        return imagem

    def insert_frame(imagem, ):
        pass
'https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi'
image_opened = Image.open(r'G:\Meu Drive\python\POO\space-chimp-ham-monkey-astronaut-grawitz-tumor.jpg')

a = Wimp(image_opened)
img = a.imagem()

image_opened = img.convert('RGBA')

print(image_opened.mode)
 """