# Serve para passar o tipo do argumento da propria class
from __future__ import annotations
from functools import partial

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0 
    
    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        return pointer
        
    def __getitem__(self, index):
        pointer = self._getnode(index)

        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out of range')
    
    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('list index out of range')

    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            else:
                pointer = pointer = pointer.next
                i +=1
        raise ValueError(f'{elem} is not in list')

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size +=1

    def remove(self, elem):
        if self.head == None:
            raise ValueError(f'{elem} is not in list')
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size -= 1
            return True
        raise ValueError(f'{elem} is not in list')

    def __repr__(self):
        r = ''
        pointer = self.head
        while(pointer):
            r += str(pointer.data) + ' -> '
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


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

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0 
    
    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        else:
            raise IndexError('The stack is empty')

    def peek(self):
        if self._size != 0:
            return self.top.data
        else:
            raise IndexError('The stack is empty')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while(pointer):
            r += str(pointer.data) + '\n'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

class Fracao:

    def __init__(self, numerador, denominador):
        self.numerador = numerador

        if denominador == 0:
            raise ValueError('O valor do denominador deve ser diferente que 0')
        else:
            self.denominador = denominador
    
    def inverter(self):
        return Fracao(self.denominador, self.numerador)

    def __neg__(self):
        return Fracao(-self.numerador, self.denominador)

    def __mul__(self, outra: Fracao):
        numerador = self.numerador * outra.numerador
        denominador = self.denominador * outra.denominador
        
        return Fracao(numerador, denominador)

    def opiop(self, outra: Fracao):
        return self.__mul__(outra.inverter())
    
    def __sub__(self, outra):
        return self.__add__(outra.negar())

    def __add__(self, outra: Fracao):
        if self.denominador == outra.denominador:
            num = self.numerador + outra.numerador
            den = self.denominador
            return Fracao(num, den)
        num = self.numerador * outra.denominador + outra.numerador*self.denominador
        den = self.denominador*outra.denominador
        return Fracao(num, den)
    
    def __str__(self):
        representacao = f'{self.numerador}/{self.denominador}'
        return representacao

    def __repr__(self):
        representacao = f'Fracao({self.numerador}, {self.denominador})'
        return representacao


class Produto:
    def __init__(self, nome_produto, preco_produto):
        self.nome = nome_produto
        self.preco = preco_produto
    
    def __add__(self, outro):
        soma_produtos = self.preco + outro.preco
        return soma_produtos
    
    def __str__(self):
        representacao_produto = f'{self.nome} R$ {self.preco}'
        return representacao_produto



# Testes
fila = Queue()
def teste():
    fila.pop()
    fila.pop()

if __name__ == '__main__':

    a = Fracao(4, 5)
    b = Fracao(3, 5)
    resultado = a * b

    

    """     fila.push('Manoel')
    fila.push('Maria')
    fila.push('Elizabete')
    fila.push('Frederico')
    fila.push('Junior')
    fila.push('Gabriel')
    fila.push('Luana') """

    

    funcao = partial(teste)
    fila.push(funcao)
    fila.push('funcao')

    fila.peek()()
    print(len(fila))