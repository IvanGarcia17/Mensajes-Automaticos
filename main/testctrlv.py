import pyautogui as pg, webbrowser as web, time as tm, pandas as pd, os as os

"""data = pd.read_csv("testcrlv.csv")
data_dict = data.to_dict('list')
telefonos = data_dict['telefono']
mensajes = data_dict['mensaje']
combo = zip(telefonos, mensajes)
first = True

for telefono, mensaje in combo:
    web.open("https://web.whatsapp.com/send?phone="+telefono+"&text="+mensaje)
    tm.sleep(12)
    if first:
        tm.sleep(7)
        first = False
    #pg.hotkey('ctrl', 'v')
    pg.press('enter')
    tm.sleep(11)
    print("enviado")
    pg.hotkey('ctrl', 'w')"""
    
web.open("https://web.whatsapp.com/send?phone=+2288521120+&text=+Hola")
tm.sleep(20)
#pg.write("Este es un msj automatico")
pg.hotkey("shift", "enter")
pg.hotkey("shift", "enter")
pg.write("Hola")
pg.hotkey("shift", "enter")
pg.hotkey("ctrl", "v")
tm.sleep(4)
pg.press("enter")
