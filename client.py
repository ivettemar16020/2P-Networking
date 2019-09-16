from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from PIL import ImageTk, Image
import tkinter
from tkinter import OptionMenu

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


def cart(path):
    imname = path
    im1 = Image.open(imname).convert("1")
    size = (im1.width // 8, im1.height // 8)
    im1 = ImageTk.BitmapImage(im1.resize(size))
    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
    val_cart = tkinter.Label(top, image=im2, bd=10)
    val_cart.pack()

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(msg)
            if "user:" in msg:
                file1 = open("user.txt","w")#write mode 
                file1.write(msg) 
                file1.close() 
                
            if "cards" in msg:
                cards_list.insert(tkinter.END, msg)
                if "2C" in msg:
                    miscartas.append('2C')
                   

                if "2D" in msg:
                    miscartas.append('2D')
                   
                if "2H" in msg:
                    miscartas.append('2H')
                

                if "2S" in msg:
                    miscartas.append('2S')
                 

                if "3C" in msg:
                    miscartas.append('3C')
                

                if "3D" in msg:
                    miscartas.append('3D')
                    

                if "3H" in msg:
                    miscartas.append('3H')
                 

                if "3S" in msg:
                    miscartas.append('3S')
            

                if "4C" in msg:
                    miscartas.append('4C')
                  

                if "4D" in msg:
                    miscartas.append('4D')
                 

                if "4H" in msg:
                    miscartas.append('4H')
                   

                if "4S" in msg:
                    miscartas.append('4S')
                    

                if "5C" in msg:
                    miscartas.append('5C')
                   
                if "5D" in msg:
                    miscartas.append('5D')
                   

                if "5H" in msg:
                    miscartas.append('5H')
                   

                if "5S" in msg:
                    miscartas.append('5S')
                    
                if "6C" in msg:
                    miscartas.append('6C')
                    

                if "6D" in msg:
                    miscartas.append('6D')
                   

                if "6H" in msg:
                    miscartas.append('6H')
                    

                if "6S" in msg:
                    miscartas.append('6S')
                   

                if "7C" in msg:
                    miscartas.append('7C')
                  

                if "7D" in msg:
                    miscartas.append('7D')
                   

                if "7H" in msg:
                    miscartas.append('7H')
                    

                if "7S" in msg:
                    miscartas.append('7S')
                    

                if "8C" in msg:
                    miscartas.append('8C')
                  

                if "8D" in msg:
                    miscartas.append('8D')
                    

                if "8H" in msg:
                    miscartas.append('8H')
                    

                if "8S" in msg:
                    miscartas.append('8S')
                   
                if "9C" in msg:
                    miscartas.append('9C')
                   

                if "9D" in msg:
                    miscartas.append('9D')
                    

                if "9H" in msg:
                    miscartas.append('9H')
                   

                if "9S" in msg:
                    miscartas.append('9S')
                    

                if "10C" in msg:
                    miscartas.append('10C')
                    

                if "10D" in msg:
                    miscartas.append('10D')
                   

                if "10H" in msg:
                    miscartas.append('10H')
                    

                if "10S" in msg:
                    miscartas.append('10S')
                   

                if "AC" in msg:
                    miscartas.append('AC')
                    

                if "AD" in msg:
                    miscartas.append('AC')
                    

                if "AH" in msg:
                    miscartas.append('AH')
                    

                if "AS" in msg:
                    miscartas.append('AS')
                  

                if "JC" in msg:
                    miscartas.append('JC')
                    

                if "JD" in msg:
                    miscartas.append('JD')
                    

                if "JH" in msg:
                    miscartas.append('JH')
                    

                if "JS" in msg:
                    miscartas.append('JS')
                    

                if "KC" in msg:
                    miscartas.append('KC')
                 

                if "KD" in msg:
                    miscartas.append('KD')
                    

                if "KH" in msg:
                    miscartas.append('KH')
                    

                if "KS" in msg:
                    miscartas.append('KS')
                    

                if "QC" in msg:
                    miscartas.append('QS')
                    

                if "QD" in msg:
                    miscartas.append('QD')
                    

                if "QH" in msg:
                    miscartas.append('QH')
                    

                if "QS" in msg:
                    miscartas.append('QS')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/QS.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor52=tkinter.Label(top, image=im2, bd=10)
                    valor52.pack()
                todascartas = (' '.join(miscartas))
                print("TODAS LAS CARTAS", todascartas)
                cartasactuales = (' '.join(miscartas[0]))
                cartasactuales1 = (' '.join(miscartas[1]))
                cartasactuales2 = (' '.join(miscartas[2]))
                cartasactuales3 = (' '.join(miscartas[3]))
                choices = {cartasactuales, cartasactuales1, cartasactuales2, cartasactuales3}
                tkvar = tkinter.StringVar()
                tkvar.set(cartasactuales) # set the default option
                popupMenu = OptionMenu(top, tkvar, *choices)
                popupMenu.pack()
                def ok():
                    #print ("Carta", tkvar.get())
                    cartasobtenidas = (' '.join(miscartas))
                    print(cartasobtenidas)
                    cartaapasar = tkvar.get()
                    cartaapasar = "cartapasar:" + cartaapasar
                    print(cartaapasar)
                    client_socket.send(bytes(cartaapasar, "utf8"))
                button2 = tkinter.Button(top, text="Pasar Carta", command=ok)
                button2.pack()
                    
                #for i in range(len(CARDS)):
                #    if CARDS[i] in msg:
                #        path = "cartas/" + CARDS[i] + ".png"
                #        cart(path)
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

top = tkinter.Tk()
top.title("Cuchara Online")
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

top.protocol("WM_DELETE_WINDOW", on_closing)
#HOST = '192.168.1.17' con el ipconfig de mi compu para conectarnos 
HOST = '127.0.0.1'
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