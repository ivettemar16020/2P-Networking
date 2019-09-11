from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from PIL import ImageTk, Image
import tkinter
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            print(msg)
            if "2C" in msg:
                img =  Image.open("cartas/2C.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel = tkinter.Label(top, image = photo)
                panel.pack()
            if "2D" in msg:
                img =  Image.open("cartas/2D.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel2 = tkinter.Label(top, image = photo)
                panel2.pack()
            if "2H" in msg:
                img =  Image.open("cartas/2H.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel3 = tkinter.Label(top, image = photo)
                panel3.pack()
            if "2S" in msg:
                img =  Image.open("cartas/2S.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel4 = tkinter.Label(top, image = photo)
                panel4.pack()
            if "3C" in msg:
                img =  Image.open("cartas/3C.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel5 = tkinter.Label(top, image = photo)
                panel5.pack()
            if "3D" in msg:
                img =  Image.open("cartas/3D.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel6 = tkinter.Label(top, image = photo)
                panel6.pack()
            if "3H" in msg:
                img =  Image.open("cartas/3H.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel7 = tkinter.Label(top, image = photo)
                panel7.pack()
            if "3S" in msg:
                img =  Image.open("cartas/3S.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel8 = tkinter.Label(top, image = photo)
                panel8.pack()
            if "4C" in msg:
                img =  Image.open("cartas/4C.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel9 = tkinter.Label(top, image = photo)
                panel9.pack()
            if "4D" in msg:
                img =  Image.open("cartas/4D.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel10 = tkinter.Label(top, image = photo)
                panel10.pack()
            if "4H" in msg:
                img =  Image.open("cartas/4H.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel11 = tkinter.Label(top, image = photo)
                panel11.pack()
            if "4S" in msg:
                img =  Image.open("cartas/4S.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel12 = tkinter.Label(top, image = photo)
                panel12.pack()
            if "5C" in msg:
                img =  Image.open("cartas/5C.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel13 = tkinter.Label(top, image = photo)
                panel13.pack()
            if "5D" in msg:
                img =  Image.open("cartas/5D.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel14 = tkinter.Label(top, image = photo)
                panel14.pack()
            if "5H" in msg:
                img =  Image.open("cartas/5H.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel15 = tkinter.Label(top, image = photo)
                panel15.pack()
            if "5S" in msg:
                img =  Image.open("cartas/5S.png")
                img = img.resize((150, 150), Image.ANTIALIAS)
                photo = tkinter.PhotoImage(file="ArtWrk.ppm") 
                panel16 = tkinter.Label(top, image = photo)
                panel16.pack()
            
        except OSError:  
            break
def send(event=None):  
    msg = my_msg.get()
    my_msg.set("")  
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()
def on_closing(event=None):
    my_msg.set("{quit}")
    send()
top = tkinter.Tk()
top.title("Cuchara Online")
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame) 
msg_list = tkinter.Listbox(messages_frame, height=15, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
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