# Criar funções de exemplo para o autoclicker.TimeoutError
import time
import pyautogui

class MotorClicker:
    #método construtor
    def __init__(self, intervalo_ms, tecla_parar, qtd_cliques, pos_x, pos_y):
        self.intervalo_ms = intervalo_ms
        self.tecla_parar = tecla_parar
        self.qtd_cliques = qtd_cliques
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rodando = False

    def clique(self):
        print('Iniciando Autoclicker em 3 segundos...')
        time.sleep(3)
        self.rodando = True
        while self.rodando:
            pyautogui.click(self.pos_x, self.pos_y)
            time.sleep(self.intervalo_ms)
    
    def parar(self):
        print('parando cliques')
    
    def ExibirInformacoesAtuais (self):
        print(self.intervalo_ms)
        print(self.tecla_parar)
        print(self.qtd_cliques)
        print(self.pos_x)
        print(self.pos_y)
    pass

