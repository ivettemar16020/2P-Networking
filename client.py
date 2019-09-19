from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from PIL import ImageTk, Image
import tkinter
from tkinter import OptionMenu
import tkinter.messagebox
import os

CARDS = [
    "2C", "2D", "2H", "2S", 
    "3C", "3D", "3H", "3S", 
    "4C", "4D", "4H", "4S", 
    "5C", "5D", "5H", "5S", 
    "6C", "6D", "6H", "6S", 
    "7C", "7D", "7H", "7S", 
    "8C", "8D", "8H", "8S", 
    "9C", "9D", "9H", "9S", 
    "10C", "10D", "10H", "10S",
    "AC", "AD", "AH", "AS",
    "JC", "JD", "JH", "JS", 
    "KC", "KD", "KH", "KS",
    "QC", "QD", "QH", "QS"]

miscartas = []
global cartas_jugador
cartas_jugador = []


def popupHalp():

    def leavemini():
        popuphelp.destroy()

    msg = "Instrucciones \nPara ganar en Cuchara Online, usted tiene que formar una mano con cuatro cartas iguales. \nPara esto, debe desechar una carta por cada turno y pasársela al siguiente jugador. \nSi usted es el último jugador del turno, entonces solo pase la carta, esta irá al desecho. \n¡Mucha suerte!\nRecuerde:\n1) Para enviar una carta, presione Pasar Carta\n2) Para recibir una carta, presione Recibir carta\n3) Si desea enviar un mensaje, escribalo y presione Send"
    popuphelp = tkinter.Tk()
    popuphelp.wm_title("Instrucciones")
    label = tkinter.Label(popuphelp, text=msg)
    label.pack(side="top", fill="x", pady = 10)
    b1 = tkinter.Button(popuphelp, text="OK", command=leavemini)
    b1.pack()
    popuphelp.mainloop()



def delete_children(cart_frame):
    for child in cart_frame.winfo_children():
        child.destroy()

def cart(path):
    cart_frame.pack(side=tkinter.LEFT, anchor=tkinter.CENTER, padx=100)
    imname = path
    im1 = Image.open(imname).convert("1")
    size = (im1.width // 8, im1.height // 8)
    im1 = ImageTk.BitmapImage(im1.resize(size))
    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
    val_cart = tkinter.Button(cart_frame, image=im2, bd=0)
    #val_cart.pack(side = tkinter.LEFT, expand=tkinter.YES)
    val_cart.image = im2
    return val_cart

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(msg)
            if  "Prueba solo para P1" in msg:
                w1 = tkinter.Label(top, text="Usuario 1")
                w1.pack()
            if  "Prueba solo para P2" in msg:
                
                w2 = tkinter.Label(top, text="Usuario 2")
                w2.pack()
            if  "Prueba solo para P3" in msg:
               
                w3 = tkinter.Label(top, text="Usuario 3")
                w3.pack()
            if  "Prueba solo para P4" in msg:
                w4 = tkinter.Label(top, text="Usuario 4")
                w4.pack()
            if "Paso el Usuario" in msg:
                print("!!!!!!!-", msg, "-!!!!!!!")
            if "turno1" in msg:
                print("RECIBIO UNA CARTA",msg)
                print("MIS CARTAS SON: ", cartas_jugador)
                nueva_carta = msg.split("turno1")[1]
                cartas_jugador.append(nueva_carta)
                las_cartitas = []
                for i in range(len(CARDS)):
                    if CARDS[i] in cartas_jugador:
                        path = "cartas/" + CARDS[i] + ".png"
                        las_cartitas.append(cart(path))
                        for j in range(len(las_cartitas)): 
                            las_cartitas[j].pack(side = tkinter.LEFT, expand=tkinter.YES, ipady=10) 

                tkvar = tkinter.StringVar()
                tkvar.set(cartas_jugador[0]) # set the default option
                popupMenu = OptionMenu(cart_frame, tkvar, *cartas_jugador)
                popupMenu.pack(side = tkinter.LEFT, expand=tkinter.YES)

                ganar(cartas_jugador)
                #ganar(["4a", "4a", "4a", "4a"])

            if "user:" in msg:
                file1 = open("user.txt","w")#write mode 
                file1.write(msg) 
                file1.close() 
                
            if "cards" in msg:
                cards_list.insert(tkinter.END, msg)
                cartitas = []
                for i in range(len(CARDS)): 
                    if CARDS[i] in msg:
                        path = "cartas/" + CARDS[i] + ".png"
                        cartitas.append(cart(path))
                        for j in range(len(cartitas)): 
                            cartitas[j].pack(side = tkinter.LEFT, expand=tkinter.YES)
                        miscartas.append(CARDS[i])
                        cartas_jugador.append(CARDS[i])
                        print(*miscartas, sep = ", ")
                   
                todascartas = (' '.join(miscartas))
                print("TODAS LAS CARTAS", todascartas)
                cartasactuales = (' '.join(miscartas[0]))
                cartasactuales1 = (' '.join(miscartas[1]))
                cartasactuales2 = (' '.join(miscartas[2]))
                cartasactuales3 = (' '.join(miscartas[3]))
                choices = {cartasactuales, cartasactuales1, cartasactuales2, cartasactuales3}
                tkvar = tkinter.StringVar()
                tkvar.set(cartasactuales) # set the default option
                popupMenu = OptionMenu(cart_frame, tkvar, *choices)
                popupMenu.pack(side = tkinter.LEFT, expand=tkinter.YES)

                def ok():
                    cartasobtenidas = (' '.join(miscartas))
                    print("Estas son las cartas obtenidas:" + cartasobtenidas)
                    cartaapasar = tkvar.get()
                    fuera = cartaapasar.replace(" ", "")
                    print("fuera", fuera)
                    print("CARTAS JUGADOR ANTES: ", cartas_jugador)
                    cartas_jugador.remove(fuera)
                    print("CARTAS JUGADOR DESPUES: ", cartas_jugador)
                    cartaapasar = "cartapasar:" + fuera
                    print(cartaapasar)
                    client_socket.send(bytes(cartaapasar, "utf8"))
                
                def refresheo(cartas):
                    print(cartas)
                    las_cartitas = []
                    for i in range(len(CARDS)):
                        if CARDS[i] in cartas_jugador:
                            path = "cartas/" + CARDS[i] + ".png"
                            las_cartitas.append(cart(path))
                            for j in range(len(las_cartitas)): 
                                las_cartitas[j].pack(side = tkinter.LEFT, expand=tkinter.YES, ipady=10) 

                    tkvar2 = tkinter.StringVar()
                    tkvar2.set(cartas_jugador[0]) # set the default option
                    popupMenu = OptionMenu(cart_frame, tkvar2, *cartas_jugador)
                    popupMenu.pack(side = tkinter.LEFT, expand=tkinter.YES)

                button2 = tkinter.Button(top, text="Pasar Carta", command=lambda:[ok(), delete_children(cart_frame), refresheo(cartas_jugador)])
                button2.pack(side = tkinter.LEFT, expand=tkinter.YES)

                def not_ok():
                    client_socket.send(bytes("recibiendo", "utf8"))

                button3 = tkinter.Button(top, text="Recibir Carta", command=lambda:[not_ok(), delete_children(cart_frame)])
                #cart_frame.pack(side=tkinter.LEFT, anchor=tkinter.CENTER)
                button3.pack(side = tkinter.LEFT, expand=tkinter.YES)

            if "cards" not in msg:
                msg_list.insert(tkinter.END, msg)
        except OSError:
            break
            
def get_user():
    #inicio de funcion para obtener usuario
    file1 = open("userget.txt","w")#write mode 
    file1.write(msg) 
    file1.close() 
        
def send(event=None):  
    msg = my_msg.get()
    if "cards" not in msg:
        my_msg.set("")  
        client_socket.send(bytes(msg, "utf8"))
        if msg == "quit":
            client_socket.close()
            top.quit()

def on_closing(event=None):
    my_msg.set("quit")
    send()

def snd1():
    os.system("b.mp4")

def ganar(cartas):  
    c1 = list(cartas[0])[0]
    c2 = list(cartas[1])[0]
    c3 = list(cartas[2])[0]
    c4 = list(cartas[3])[0]
    print("los valorcillos: ", c1, c2, c3, c4)
    if c1 == c2 == c3 == c4:
        print("Ganaste, debes presionar el boton")
        win_button.configure(state=tkinter.NORMAL)
    else: 
        print("Tu mano no es valida para ganar")

def show_msg(m1, m2):
   tkinter.messagebox.showinfo(m1, m2)

top = tkinter.Tk()
top.title("Cuchara Online")
var = tkinter.IntVar()
rb1 = tkinter.Radiobutton(top, text= "Video de Instrucciones", variable = var, value=1, command=snd1)
rb1.pack()
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame) 
msg_list = tkinter.Listbox(messages_frame, height=8, width=100, yscrollcommand=scrollbar.set)
cards_list = tkinter.Listbox(messages_frame, height=8, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
cards_list.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
cards_list.pack()
messages_frame.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
cart_frame = tkinter.Frame(top)
cart_frame.pack(side=tkinter.LEFT, anchor=tkinter.CENTER)


###GANAR BOTON 
bottomframe = tkinter.Frame(top)
bottomframe.pack( side=tkinter.BOTTOM, anchor=tkinter.SE)

imname = "assets/spoon.png"
origin = Image.open(imname).convert("1")
size = (origin.width // 3, origin.height // 3)
origin = ImageTk.BitmapImage(origin.resize(size))
spoon = ImageTk.PhotoImage(Image.open(imname).resize(size))
win_button = tkinter.Button(bottomframe, image = spoon, state=tkinter.DISABLED)
#win_button = tkinter.Button(bottomframe, image = spoon, state=tkinter.DISABLED, command = show_msg("Felicidades", "¡Ganaste el juego!"))
win_button.pack(side=tkinter.RIGHT)

upperframe = tkinter.Frame(top)
upperframe.pack(side=tkinter.TOP, anchor=tkinter.NE)

helpim = "assets/help.png"
originim = Image.open(helpim).convert("1")
sizes = (originim.width // 10, originim.height // 10)
originim = ImageTk.BitmapImage(originim.resize(sizes))
halpicon = ImageTk.PhotoImage(Image.open(helpim).resize(sizes))
halpbutton = tkinter.Button(upperframe, image = halpicon, command=popupHalp)
halpbutton.pack(side=tkinter.RIGHT)

top.protocol("WM_DELETE_WINDOW", on_closing)
#HOST = '192.168.1.17' con el ipconfig de mi compu para conectarnos 
#HOST = '127.0.0.1'
HOST = '10.200.100.112'
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  