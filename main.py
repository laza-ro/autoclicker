import tkinter as tk
from interface import AppInterface
import os
import sys

def caminho_icon (caminho_dif):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath (".")
    return os.path.join(base_path, caminho_dif)

root = tk.Tk() #cria a janela do sistema 

try:
    caminho_do_icone = caminho_icon("icon.ico")
    root.iconbitmap(caminho_do_icone)
except Exception as e:
    print(f"Erro ao carregar icone:{e}")

app = AppInterface(root) # cria a interface gráfica do interface.py
root.mainloop() #mantém a janela aberta