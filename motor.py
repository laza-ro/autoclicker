# Criar funções de exemplo para o autoclicker.
import time
import pyautogui
import keyboard

pyautogui.PAUSE = 0

class MotorClicker:
    #método construtor
    def __init__(self, intervalo_ms, tecla_parar, pos_x, pos_y):
        self.intervalo_segundos = intervalo_ms / 1000 #conversao de ms para segundos
        self.tecla_parar = tecla_parar
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rodando = False

    def iniciar(self):
        print('Iniciando Autoclicker em 3 segundos...')
        time.sleep(3)
        self.rodando = True
        keyboard.add_hotkey(self.tecla_parar, self.parar)
        while self.rodando:
            pyautogui.click(self.pos_x, self.pos_y)
            time.sleep(self.intervalo_segundos)
    
    def parar(self):
        self.rodando = False
        print ('Autoclicker parado!')

    # def ExibirInformacoesAtuais (self):
    #     print(self.intervalo_segundos)
    #     print(self.tecla_parar)
    #     print(self.pos_x)
    #     print(self.pos_y)


