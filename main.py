import tkinter as tk
from interface import AppInterface

root = tk.Tk () #cria a janela do sistema 
app = AppInterface(root) # cria a interface gráfica do interface.py

root.mainloop () #mantém a janela aberta


