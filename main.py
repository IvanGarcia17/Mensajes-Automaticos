import pyautogui as pg, webbrowser as web, time as tm, emoji
import pandas as pd

data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
telefonos = data_dict['telefono']
mensajes = data_dict['mensaje']
combo = zip(telefonos, mensajes)
first = True

"""web.open("https://web.whatsapp.com/send?phone="+telefono+"&text="+mensaje)
tm.sleep(20)"""

"""pg.write("Este es un msj automatico")
pg.press('enter')
pg.write("Hola")"""

"""pg.hotkey('shift', 'enter')"""

"""web.close("https://web.whatsapp.com/send?phone=+52 1 228 235 9014")"""
"""pg.write("Test")
pg.press('enter')
tm.sleep(30)
pg.hotkey('ctrl', 'w')
web.open("https://web.whatsapp.com/send?phone=+52 1 228 235 9014&text=🤩🌈COLORS RUN🌈🌕\n\n\n🔴🟠🟡🟢🔵🟣🟤\n\nTe presentamos la CONVOCATORIA oficial de esta divertida y colorida carrera🤩🤗\n\n7 km🛣️ nocturnos✨🌙 llenos de emoción y color🤗\n📅12 de agosto de 2022 \n📍Teocelo, Ver.  \n🕗8:00 pm. \n\nPremiación en EFECTIVO 💰 por igual a las 3 categorías👟 participantes y ambas ramas varonil y femenil🚻: \n\n▫️Juvenil (menores de 17 años)\n▫️Libre (18 a 39 años) \n▫️Máster (40 años en adelante) \n\n🥇1er Lugar: $1,000.°°\n🥈2do Lugar: $800.°° \n🥉3er Lugar: $500.°°\n\n📝Adquiere tu folio en la secretaría del Ayuntamiento o vía WhatsApp  al ☎️2282433307 depositando a la cuenta: \n\n💳Transferencia electrónica:\nCuenta bancaria: 18-00020901-1 \nCLABE: 014840180002090113 Banco: SANTANDER\nTitular: Municipio de Teocelo, Ver.\n\n\n🌌Recuerda que la vida es del color que tú la quieras soñar !!!! 💫\n\n\n#TeoceloRun\n#PacerTime")
tm.sleep(20)
pg.hotkey('shift', 'enter')
pg.write("Test 🤩🌈COLORS RUN🌈🌕")
pg.write("🔴🟠🟡🟢🔵🟣🟤")
pg.write("Te presentamos la CONVOCATORIA oficial de esta divertida y colorida carrera🤩🤗")"""
"""emoji.emoj
ize(":zipper-mouth_face:")"""

"""pg.press('enter')"""

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


    #Copiado de whats app
    #Copiado de whats app2
    #Windows
    #Copiado de escribir
