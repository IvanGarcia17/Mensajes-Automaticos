import pyautogui as pg, webbrowser as web, time as tm, pandas as pd, os as os

data = pd.read_csv("resultadosCSSA2022.csv")
data_dict = data.to_dict('list')
#no = data_dict['numero']
telefonos = data_dict['telefono']
mensajes = data_dict['mensaje']
combo = zip(telefonos, mensajes)
first = True
#contador = int(1)
#conta = str((contador))
x = 1
x = x+1

#cur = dir(os)
#for i in cur:
#    count = 1
#    count += 1

for telefono, mensaje in combo:
    web.open("https://web.whatsapp.com/send?phone="+telefono+"&text="+mensaje)
    tm.sleep(12)
    if first:
        tm.sleep(7)
        first = False
    #tm.sleep(4)
    pg.press('enter')
    tm.sleep(11)
    pg.hotkey('ctrl', 'w')
    #print("enviado ")
    #for i in [1]:
    #    print(f"Enviado {i+1}")
    print("enviado")
    #print("enviado", count, i)
    #sumador = int(contador+1)
    #print(sumador)
    #print(str(contador))
