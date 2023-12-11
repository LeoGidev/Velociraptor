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

ventana = tkinter.Tk()
ventana.attributes('-fullscreen',True)
ventana.overrideredirect(True)
ventana.overrideredirect(False)
ventana.geometry('400x400')
ventana.title('velocidad')
imagen = PhotoImage(file="logo.png")
Label(ventana,  bd=0).pack()


Button(ventana,  width=150, height=150, borderwidth=1, command=test().pack()

mensaje = StringVar()
mensaje.set('Por favor, presione el boton verde para comenzar el la prueba')
monitor=Label(ventana, textvar=mensaje)
monitor.pack()

mensaje2 = StringVar()
mensaje2.set('')
monitor2=Label(ventana, textvar=mensaje2)
monitor2.pack()

exit_b=Button(ventana, text='Salir', command=ventana.destroy)
exit_b.pack(pady=20)

ventana.mainloop()