from turtle import width
import pyautogui as pg, webbrowser as wb, time as tm, pandas as pd, os as os

data = pd.read_csv("resultadosINVITACION-SR.csv", encoding= 'unicode_escape')
data_dict = data.to_dict('list')
telefonos = data_dict['telefono']
mensajes = data_dict['mensaje']
combo = zip(telefonos, mensajes)
first = True

for telefono, mensaje in combo:
    wb.open("https://web.whatsapp.com/send?phone="+telefono+"&text="+mensaje)
    tm.sleep(11)
    if first:
        first = False
    tm.sleep(32)
    pg.click()
    pg.hotkey('ctrl', 'v')
    tm.sleep(8)
    pg.press('enter')
    tm.sleep(7)
    pg.hotkey('ctrl', 'w')
    print("enviado")