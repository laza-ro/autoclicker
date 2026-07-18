from PIL import GimpGradientFile
import tkinter as tk

class AppInterface:
    def __init__(self): #criando a tela principal do projeto
        self.tela = tk.Tk()
        self.tela.title ("Auto Clicker")
        self.tela.geometry("400x400")
        self.tela.resizable(True, True)

    #desenho do projeto
        #espaço pra inserir os valores de ms
        self.label_ms = tk.Label(self.tela, text="Intervalo em ms")
        self.label_ms.pack(pady = 5) #espaço nas bordas
        self.entrada_ms = tk.Entry(self.tela)
        self.entrada_ms.pack()
        #espaço pra inserir a posição X na tela
        self.label_pos_x = tk.Label(self.tela, text = "Posição X")
        self.label_pos_x.pack(pady = 5) #espaço nas bordas
        self.entrada_pos_x = tk.Entry(self.tela)
        self.entrada_pos_x.pack()
        #espaço pra inserir a posição Y na tela
        self.label_pos_y = tk.Label(self.tela, text = "Posição Y")
        self.label_pos_y.pack(pady = 5) #espaço nas bordas
        self.entrada_pos_y = tk.Entry(self.tela)
        self.entrada_pos_y.pack()
        #espaço pra hotkey
        self.label_tecla_parar = tk.Label(self.tela, text = "Insira a tecla de atalho para parar")
        self.label_tecla_parar.pack(pady = 5)
        self.entrada_tecla_parar = tk.Entry(self.tela)
        self.entrada_tecla_parar.pack()
    #criação dos botões
        #botão iniciar
        self.btn_iniciar = tk.Button (self.tela, text = "Iniciar", command=self.iniciar_clicker())
        self.btn_iniciar.pack(pady = 10)
        #botão parar
        self.btn_parar = tk.Button (self.tela, text = "Parar", command = self.parar_clicker())
        self.btn_parar.pack(pady=10)
        #capturar posição (tela)
        self.btn_capturar_posicao = tk.Button (self.tela, text = "Capturar posição", command = self.capturar_posicao())
        self.btn_capturar_posicao.pack(pady = 10)