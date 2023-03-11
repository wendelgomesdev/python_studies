import locale
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from PIL import ImageTk, Image
from tkcalendar import *
from datetime import date
from decimal import Decimal

class Janela(Tk):
    def __init__(self, titulo, cor_fundo='white', largura='300', altura='300'):
        super().__init__()

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        eixo_x = (int(largura_tela) // 2) - (int(largura) // 2)
        eixo_y = (int(altura_tela) // 2) - (int(altura) // 2)

        self.geometry(f'{largura}x{altura}+{eixo_x}+{eixo_y}')

        self.title(titulo)

        self.configure(background=cor_fundo)

    def fechar_janela(self):
        self.destroy()

    def trocar_titulo_janela(self, titulo_novo):
        self.title(titulo_novo)

    def redimencionar_janela(self, largura='300', altura='300'):
        # Centralizar janela na tela
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        eixo_x = (int(largura_tela) // 2) - (int(largura) // 2)
        eixo_y = (int(altura_tela) // 2) - (int(altura) // 2)
        eixo_x = (int(largura_tela) // 2) - (int(largura) // 2)
        eixo_y = (int(altura_tela) // 2) - (int(altura) // 2)
        # Tamanho e posição na tela
        self.geometry(f'{largura}x{altura}+{eixo_x}+{eixo_y}')

    def minimizar_janela(self):
        self.iconify()
    
    def restaurar_janela(self):
        self.deiconify()
        
class Quadro(Frame):
    def __init__(self, janela, eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(janela)

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

    def deletar_quadro(self):
        self.pack_forget()


class Etiqueta(Label):
    def __init__(self, frame, texto, eixo_x=0, eixo_y=0):
        super().__init__(frame)
        self['text'] = texto

        self.place(relx=eixo_x, rely=eixo_y)
    
    def deletar_etiqueta(self):
        self.pack_forget()


class Botao(Button):
    def __init__(self, frame, texto, comando, eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)
        self['text'] = texto
        self['command'] = comando

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

    def deletar_botao(self):
        self.pack_forget()


class CaixaTexto(Entry):
    def __init__(self, frame, placeholder='desligado', eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

    def deletar_campo(self):
        self.pack_forget()

    def limpar_campo(self):
        self.delete(0, 'end')

    def inserir_texto(self, texto):
        self.delete(0, END)
        self.insert(0, texto)


class ListaOpcoes(ttk.Combobox):
    def __init__(self, frame, lista=False, funcao_digitar=False, valor_padrao='desligado', eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)
        
        if lista != False:
            self['value'] = lista

        if funcao_digitar == False:
            self['state'] = 'readonly'

        if valor_padrao != 'desligado':
            self.current(valor_padrao)

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

    def deletar_listaopcoes(self):
        self.pack_forget()

    def alterar_opcao_selecionada(self, indice_opcao):
        self.current(indice_opcao)

    def recaregar_lista(self, nova_lista):
        self['value'] = nova_lista

class CaixaMarcacao(ttk.Checkbutton):
    def __init__(self, frame, texto, comando=False, eixo_x=0, eixo_y=0, iniciar_escondido=False):
        super().__init__(frame)

        self.variavel = IntVar()
        self['text'] = texto
        self['variable'] = self.variavel

        self.x = eixo_x
        self.y = eixo_y

        if iniciar_escondido == False:
            self.place(relx=self.x, rely=self.y)

        if comando != False:
            self['command'] = comando
    
    def esconder_caixa_marcacao(self):
        self.place_forget()

    def exibir_caixa_marcacao(self):
        self.place(relx=self.x, rely=self.y)

class CaixaErro:
    def __init__(self, mensagem):
        self.caixa_erro = messagebox.showerror(title='Erro', message=mensagem)


class CaixaMensagem:
    def __init__(self, mensagem):
        self.caixa_erro = messagebox.showinfo(
            title='Informação', message=mensagem)


class BarraProgresso(ttk.Progressbar):
    def __init__(self, frame, formato, tamanho, modo, eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)

        self['orient'] = formato  # HORIZONTAL
        self['length'] = tamanho
        self['mode'] = modo  # 'determinate' / 'indeterminate'

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

    def esconder_barra_progresso(self):
        self.place_forget()


class AbrirImagem(Label):
    def __init__(self, frame, escala_imagem, caminho_imagem=False, eixo_x=0, eixo_y=0):
        super().__init__(frame)

        self.escala_imagem = escala_imagem

        if caminho_imagem != False:
            # Abrir imagem com caminho passado
            self.abrir_imagem = Image.open(caminho_imagem)

            with Image.open(caminho_imagem) as imagem_aberta:
                # pegar largura da imagem
                largura_imagem = round(imagem_aberta.size[0]*self.escala_imagem)
                altura_imagem = round(imagem_aberta.size[1]*self.escala_imagem)

            self.imagem_atual_carregada = ImageTk.PhotoImage(
                self.abrir_imagem.resize((largura_imagem, altura_imagem)))

            # Criar uma Label e exibir imagem na janela
            self['image'] = self.imagem_atual_carregada

        self.place(relx=eixo_x, rely=eixo_y)



    def deletar_imagem(self):
        self.pack_forget()

    def alterar_imagem(self, nova_imagem):
        self.abrir_imagem = Image.open(nova_imagem)

        with Image.open(nova_imagem) as imagem_aberta:
            # pegar largura da imagem
            largura_imagem = round(imagem_aberta.size[0]*self.escala_imagem)
            altura_imagem = round(imagem_aberta.size[1]*self.escala_imagem)

        self.imagem_atual_carregada = ImageTk.PhotoImage(
            self.abrir_imagem.resize((largura_imagem, altura_imagem)))

        # Criar uma Label e exibir imagem na janela
        self['image'] = self.imagem_atual_carregada


class CaixaTextoLongo(Text):
    def __init__(self, frame, texto=False, eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)
        self['font'] = ('Helvetica', 12)
        self['selectbackground'] = 'yellow'
        self['selectforeground'] = 'black'
        self['undo'] = True

        self.barra_rolagem = Scrollbar(frame)

        self['yscrollcommand'] = self.barra_rolagem.set

        if texto != False:
            self.insert(INSERT, texto)

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

        self.barra_rolagem.place(relx=(largura + 0.03), rely=eixo_y,
                                 relwidth=0.04, relheight=altura)

        self.barra_rolagem.config(command=self.yview)

    def alterar_texto(self, texto_novo):
        if texto_novo != False:
            self.deletar_texto()
            self.insert(INSERT, texto_novo)

    def deletar_texto(self):
        self.delete('1.0', END)


class BarraRolagem(Scrollbar):
    def __init__(self, frame, direcao_rolagem,  eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)
        self['fill'] = direcao_rolagem

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)


class Tabela(ttk.Treeview):
    def __init__(self, *colunas, frame, barra_rolagem_orientacao='vertical', eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)
        self['column'] = colunas
        # criar coluna vazia no inicio
        self.heading('#0', text='')
        self.column('#0', width=1)

        if len(colunas) > 0:
            for indice_coluna, coluna in enumerate(colunas):
                self.heading(f'#{indice_coluna+1}', text=coluna)

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

        # barra de rolagem
        self.barra_rolagem = Scrollbar(frame, orient=barra_rolagem_orientacao)
        self.configure(yscroll=self.barra_rolagem.set)

        self.barra_rolagem.place(relx=(largura + 0.01), rely=eixo_y,
                                 relwidth=0.04, relheight=altura)


    def comando_clique(self, cliques, comando):
        self.bind(f'<{cliques}>', comando)
        # comandos:
        # Double-1.

class Grupo(LabelFrame):
    def __init__(self, frame, texto, eixo_x=0, eixo_y=0, largura=0, altura=0):
        super().__init__(frame)
        self['text'] = texto

        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)

    def deletar_grupo(self):
        self.pack_forget()
    
class BalaoInformativo(Label):
    def __init__(self, frame, cor_fundo='#cccccc'):
        super().__init__(frame)

        
        self.configure(background=cor_fundo)

    def exibir_balao(self, texto):
        self['text'] = texto
        self.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.1, anchor=CENTER)

    def esconder_balao(self):
        self.place_forget()

class Calendario(Calendar):
    def __init__(self, frame, modo_selecao='day', eixo_x=0, eixo_y=0, largura=0, altura=0, padrao_data='pt_br'):
        super().__init__(frame, selectmode=modo_selecao, locale=padrao_data)
        
        self.place(relx=eixo_x, rely=eixo_y,
                   relwidth=largura, relheight=altura)
    
    def esconder_calendario(self):
        self.place_forget()

    def alterar_data(self, dia, mes, ano):

        self.selection_set(date(ano, mes, dia))

class JanelaProgresso(Janela):
    def __init__(self, texto_acao, titulo_janela, largura_janela=300, altura_janela=100, modo_progresso='determinate', quantidade_etapas=100):
        super().__init__(titulo=titulo_janela, largura=largura_janela, altura=altura_janela)
        
        self.quantidade_etapas_total = quantidade_etapas
        self.indice_etapa = 100 / self.quantidade_etapas_total
        self.contador = 1

        self.verificar_termino = (100 / quantidade_etapas) * quantidade_etapas
        self.quadro_principal = Quadro(self, eixo_x=0, eixo_y=0, largura=1, altura=1)
        self.texto_progresso = Etiqueta(self, texto=texto_acao, eixo_x=0.1, eixo_y=0.12)
        self.barra_carregando = BarraProgresso(self, formato=HORIZONTAL, modo=modo_progresso, tamanho=100, eixo_x=0.1, eixo_y=0.35, largura=0.8, altura=0.3)

    def dar_passo(self):
        self.barra_carregando['value'] =  self.barra_carregando['value'] + self.indice_etapa
        self.update_idletasks()
        
        if self.contador == self.quantidade_etapas_total:
            self.barra_carregando['value'] = 100
            self.after(600, self.destroy)
        else:
            self.contador += 1
    