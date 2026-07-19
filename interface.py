import tkinter as tk
import pyautogui
import time
from motor import MotorClicker
import threading

class AppInterface:
    def __init__(self, root): #criando a tela principal do projeto
        self.root = root
        self.root.title ("Auto Clicker")
        self.root.geometry("400x400")
        self.root.resizable(True, True)
        

    #desenho do projeto
        #espaço pra inserir os valores de ms
        self.label_ms = tk.Label(self.root, text="Intervalo em ms")
        self.label_ms.pack(pady = 5) #espaço nas bordas
        self.entrada_ms = tk.Entry(self.root)
        self.entrada_ms.pack()
        #espaço pra inserir a posição X na tela
        self.label_pos_x = tk.Label(self.root, text = "Posição X")
        self.label_pos_x.pack(pady = 5) #espaço nas bordas
        self.entrada_pos_x = tk.Entry(self.root)
        self.entrada_pos_x.pack()
        #espaço pra inserir a posição Y na tela
        self.label_pos_y = tk.Label(self.root, text = "Posição Y")
        self.label_pos_y.pack(pady = 5) #espaço nas bordas
        self.entrada_pos_y = tk.Entry(self.root)
        self.entrada_pos_y.pack()
        #espaço pra hotkey
        self.label_tecla_parar = tk.Label(self.root, text = "Insira a tecla de atalho para parar")
        self.label_tecla_parar.pack(pady = 5)
        self.entrada_tecla_parar = tk.Entry(self.root)
        self.entrada_tecla_parar.pack()
        #criação dos botões
        #botão iniciar
        self.btn_iniciar = tk.Button (self.root, text = "Iniciar", command=self.iniciar_clicker)
        self.btn_iniciar.pack(pady = 10)
        #botão parar
        self.btn_parar = tk.Button (self.root, text = "Parar", command = self.parar_clicker)
        self.btn_parar.pack(pady=10)
        #capturar posição (tela)
        self.btn_capturar_posicao = tk.Button (self.root, text = "Capturar posição", command = self.capturar_posicao)
        self.btn_capturar_posicao.pack(pady = 10)

        ##rodapé
        self.label_rodape = tk.Label (
            self.root,
            text="Desenvolvido por laza-ro | v1.0",
            font = ("Times New Roman", 8),
            fg="gray"
        )
        self.label_rodape.pack(side=tk.BOTTOM, pady=10)

        self.root.mainloop()

    #funções dos botões criados anteriormente
    def iniciar_clicker(self):
        print("Iniciando!")
        pos_x = int(self.entrada_pos_x.get()) #convertendo de string pra int
        pos_y = int(self.entrada_pos_y.get()) #convertendo de string pra int
        intervalo_ms = int(self.entrada_ms.get()) #convertendo de string pra int
        tecla_parar = self.entrada_tecla_parar.get() #não precisa converter porque é o mesmo que um texto
        self.motor = MotorClicker(intervalo_ms, tecla_parar, pos_x, pos_y) #o self.motor é usado para que guarde a informação do motor na memória
        threading.Thread(target=self.motor.iniciar, daemon = True).start()
        #threading.Thread cria uma linha de execução temporária pra assumir a tarefa em paralelo de iniciar o motor. o daemon serve pra que o programa não feche enquanto o thread estiver rodando
        #passar o motor.iniciar com os parênteses iria fazer com que a função fosse executada imediatamente antes de entrar no threading.Thread
        #daemon = true significa que a thread é temporária, ou seja, ela será encerrada junto com o programa principal ao ser fechado

    def parar_clicker(self):
        print("Parando!")
        self.motor.parar()

    def capturar_posicao(self):
        print("Capturando posição na tela...")
        time.sleep(3)
        posicao = pyautogui.position()
        self.entrada_pos_x.delete(0, "end")
        self.entrada_pos_y.delete(0, "end")
        self.entrada_pos_x.insert(0, posicao[0])
        self.entrada_pos_y.insert(0, posicao[1])
        print("Posição encontrada")

if __name__ == "__main__":
    AppInterface()