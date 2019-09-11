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
                imname = "cartas/2C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor3=tkinter.Label(top, image=im2, bd=10)
                valor3.pack()
            if "2D" in msg:
                imname = "cartas/2D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor3=tkinter.Label(top, image=im2, bd=10)
                valor3.pack()
            if "2H" in msg:
                imname = "cartas/2H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor4=tkinter.Label(top, image=im2, bd=10)
                valor4.pack()
            if "2S" in msg:
                imname = "cartas/2S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor5=tkinter.Label(top, image=im2, bd=10)
                valor5.pack()
            if "3C" in msg:
                imname = "cartas/3C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor6=tkinter.Label(top, image=im2, bd=10)
                valor6.pack()
            if "3D" in msg:
                imname = "cartas/3D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor7=tkinter.Label(top, image=im2, bd=10)
                valor7.pack()
            if "3H" in msg:
                imname = "cartas/3H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor8=tkinter.Label(top, image=im2, bd=10)
                valor8.pack()
            if "3S" in msg:
                imname = "cartas/3S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor9=tkinter.Label(top, image=im2, bd=10)
                valor9.pack()
            if "4C" in msg:
                imname = "cartas/4C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor10=tkinter.Label(top, image=im2, bd=10)
                valor10.pack()
            if "4D" in msg:
                imname = "cartas/4D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor11=tkinter.Label(top, image=im2, bd=10)
                valor11.pack()
            if "4H" in msg:
                imname = "cartas/4H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor12=tkinter.Label(top, image=im2, bd=10)
                valor12.pack()
            if "4S" in msg:
                imname = "cartas/4S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor13=tkinter.Label(top, image=im2, bd=10)
                valor13.pack()
            if "5C" in msg:
                imname = "cartas/5C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor14=tkinter.Label(top, image=im2, bd=10)
                valor14.pack()
            if "5D" in msg:
                imname = "cartas/5D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor15=tkinter.Label(top, image=im2, bd=10)
                valor15.pack()
            if "5H" in msg:
                imname = "cartas/5H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor16=tkinter.Label(top, image=im2, bd=10)
                valor16.pack()
            if "5S" in msg:
                imname = "cartas/5S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor17=tkinter.Label(top, image=im2, bd=10)
                valor17.pack()
            
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