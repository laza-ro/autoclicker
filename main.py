import pyautogui
import time

print('Será iniciado em 5 segundos...')
time.sleep(5)

for i in range(100):
    pyautogui.click()
    time.sleep(2)  # segundos