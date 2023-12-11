import speedtest
import math
import requests
import tkinter
from tkinter import*
from tkinter import ttk

def test():
    st = speedtest.Speedtest()
    d_st = st.download()/1000000
    dwnT = round(d_st,2)
    u_st = st.upload()/1000000
    upldT = round(u_st,2)
    print("tu velocidad es", dwnT, "Mbs")
    print("tu subida es", upldT, "Mbs")
    st.get_servers([])
    ping = st.results.ping
    print("tu ping es de", ping)
    compDwn= 'descarga: ' + str(dwnT) + ' mbs \n ' + 'subida: ' + str(upldT) + ' mbs \n ping: ' + str(ping)
    #requests.post('https://api.telegram.org/[BOTTOKEN]/sendMessage',data={'chat_id': '[CHATID]', 'text': 'Resultado de la prueba:'})
    #requests.post('https://api.telegram.org/[BOTTOKEN]/sendMessage',data={'chat_id': '[CHATID]', 'text': compDwn})
    mensaje.set(compDwn)
    mensaje2.set('listo')

