import pyautogui as pg, webbrowser as web, time as tm, pandas as pd

data = pd.read_csv("resultadosCSSA2022.csv")
data_dict = data.to_dict('list')
telefonos = data_dict['telefono']
mensajes = data_dict['mensaje']
combo = zip(telefonos, mensajes)
first = True
contador = int(str(1))
conta = (contador+1)

for telefono, mensaje in combo:
    web.open("https://web.whatsapp.com/send?phone="+telefono+"&text="+mensaje)
    tm.sleep(12)
    if first:
        tm.sleep(7)
        first = False
    #tm.sleep(4)
    pg.press('enter')
    tm.sleep(10)
    pg.hotkey('ctrl', 'w')
    print("enviado")
    print(conta)