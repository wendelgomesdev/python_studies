import time
from tkinter import * 

def escrever():
        print('teste ok')

root = Tk()
teste_frame = Frame(root)
teste_frame.pack()

# - Classe
# classe se refere a uma ideia abstrata, uma molde de algum objeto
# aqui possui todas as caracteristicas dessa categoria
class Botao(Button):
    def __init__(self, frame, texto, comando, lado):
        super().__init__(master=frame)
        self['text'] = texto
        self['command'] = comando
        self.pack(side=lado)

# - Objeto / Instância
# objeto ou instacia ja esta relacionado com algo concreto, algo que carrega todas as 
# caracteriscas da classe, mas neste caso se refere a uma coisa especifica e não generica
botao_teste = Botao(teste_frame, 'teste', escrever,LEFT)


# - Atributo
# todo objeto possui suas caracteristicas, suas peculiaridades, por exemplo, cor, tamanho e etc.
""" self['text'] = texto
self['command'] = comando
self.pack(side=lado) """


# - Método
# um objeto também possui suas ações por exemplo um botão pode desligar algo, almentar o volume e etc.
class Botao(Button):
    def __init__(self, frame, texto, comando, lado):
        super().__init__(master=frame)
        self['text'] = texto
        self['command'] = comando
        self.pack(side=lado)

    def deletar_botao(self):
        self.pack_forget()

# - Mensagem
# se refere a uma chamada de um metodo de algum objeto
botao_teste2 = Botao(teste_frame, 'Teste2', escrever,LEFT)
root.after(5000, botao_teste2.deletar_botao)

# - Herança
# Por exemplo um botao, um botao deletar para ser mais espesifico, se trata de um botao generico 
# que por sua fez possuem carateristicas particulares com os outros botoes por exemplo ser precionado

""" class Botao(Button):
    def __init__(self, frame, texto, comando, lado):
        super().__init__(master=frame)
        self['text'] = texto
        self['command'] = comando
        self.pack(side=lado)

    def deletar_botao(self):
        self.pack_forget() """
# No exemplo acima todo botao possui uma função deletar_botao 
# se trata de uma herança da classe botao

# - Associação
# Podemos utilizar recursos de outros objetos, 
# por exemplo o botão possui um estilo.


# - Polimorfismo
# as mesmas operações podem se comportar de forma 
# diferente em classes diferentes
# por exemplo, podemos ter uma mesma super casse 
# onde os mesmos metodos se comportantam diferente em cada classe


# - Encapsulaento
# serve para esconder atributos de um objeto


# ===============================================

# Algumas anotações:

# # self é a referencia para o proprio o objto qeu chamou o metodo 

root.mainloop()