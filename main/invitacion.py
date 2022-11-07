import pyautogui as pg, webbrowser as web, time as tm, emoji
import pandas as pd

data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
telefonos = data_dict['telefono']
mensajes = data_dict['mensaje']
combo = zip(telefonos, mensajes)
first = True

for telefono, mensaje in combo:
    web.open("https://web.whatsapp.com/send?phone="+telefono+"&text="+mensaje)
    tm.sleep(20)
    if first:
        tm.sleep(7)
        first = False
    tm.sleep(7)
    pg.press('enter')
    tm.sleep(16)
    pg.hotkey('ctrl', 'w')