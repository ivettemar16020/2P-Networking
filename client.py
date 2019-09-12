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
            if "6C" in msg:
                imname = "cartas/6C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor18=tkinter.Label(top, image=im2, bd=10)
                valor18.pack()
            if "6D" in msg:
                imname = "cartas/6D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor19=tkinter.Label(top, image=im2, bd=10)
                valor19.pack()
            if "6H" in msg:
                imname = "cartas/6H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor20=tkinter.Label(top, image=im2, bd=10)
                valor20.pack()
            if "6S" in msg:
                imname = "cartas/6S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor21=tkinter.Label(top, image=im2, bd=10)
                valor21.pack()
            if "7C" in msg:
                imname = "cartas/7C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor22=tkinter.Label(top, image=im2, bd=10)
                valor22.pack()
            if "7D" in msg:
                imname = "cartas/7D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor23=tkinter.Label(top, image=im2, bd=10)
                valor23.pack()
            if "7H" in msg:
                imname = "cartas/7H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor24=tkinter.Label(top, image=im2, bd=10)
                valor24.pack()
            if "7S" in msg:
                imname = "cartas/7S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor25=tkinter.Label(top, image=im2, bd=10)
                valor25.pack()
            if "8C" in msg:
                imname = "cartas/8C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor26=tkinter.Label(top, image=im2, bd=10)
                valor26.pack()
            if "8D" in msg:
                imname = "cartas/8D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor27=tkinter.Label(top, image=im2, bd=10)
                valor27.pack()
            if "8H" in msg:
                imname = "cartas/8H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor28=tkinter.Label(top, image=im2, bd=10)
                valor28.pack()
            if "8S" in msg:
                imname = "cartas/8S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor29=tkinter.Label(top, image=im2, bd=10)
                valor29.pack()
            if "9C" in msg:
                imname = "cartas/9C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor30=tkinter.Label(top, image=im2, bd=10)
                valor30.pack()
            if "9D" in msg:
                imname = "cartas/9D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor31=tkinter.Label(top, image=im2, bd=10)
                valor31.pack()
            if "9H" in msg:
                imname = "cartas/9H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor32=tkinter.Label(top, image=im2, bd=10)
                valor32.pack()
            if "9S" in msg:
                imname = "cartas/9S.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor33=tkinter.Label(top, image=im2, bd=10)
                valor33.pack()
            if "10C" in msg:
                imname = "cartas/9C.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor34=tkinter.Label(top, image=im2, bd=10)
                valor34.pack()
            if "10D" in msg:
                imname = "cartas/10D.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor35=tkinter.Label(top, image=im2, bd=10)
                valor35.pack()
            if "10H" in msg:
                imname = "cartas/10H.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor36=tkinter.Label(top, image=im2, bd=10)
                valor36.pack()
            if "10S" in msg:
                imname = "cartas/AS.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor37=tkinter.Label(top, image=im2, bd=10)
                valor37.pack()
            if "AC" in msg:
                imname = "cartas/AC.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor38=tkinter.Label(top, image=im2, bd=10)
                valor38.pack()
            if "AD" in msg:
                imname = "cartas/AD.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor39=tkinter.Label(top, image=im2, bd=10)
                valor39.pack()
            if "AH" in msg:
                imname = "cartas/AH.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor40=tkinter.Label(top, image=im2, bd=10)
                valor40.pack()
            if "AS" in msg:
                imname = "cartas/AS.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor41=tkinter.Label(top, image=im2, bd=10)
                valor41.pack()
            if "JC" in msg:
                imname = "cartas/JC.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor42=tkinter.Label(top, image=im2, bd=10)
                valor42.pack()
            if "JD" in msg:
                imname = "cartas/JD.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor43=tkinter.Label(top, image=im2, bd=10)
                valor43.pack()
            if "JH" in msg:
                imname = "cartas/JH.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor43=tkinter.Label(top, image=im2, bd=10)
                valor43.pack()
            if "JS" in msg:
                imname = "cartas/JS.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor44=tkinter.Label(top, image=im2, bd=10)
                valor44.pack()
            if "KC" in msg:
                imname = "cartas/KC.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor45=tkinter.Label(top, image=im2, bd=10)
                valor45.pack()
            if "KD" in msg:
                imname = "cartas/KD.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor46=tkinter.Label(top, image=im2, bd=10)
                valor46.pack()
            if "KH" in msg:
                imname = "cartas/KH.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor47=tkinter.Label(top, image=im2, bd=10)
                valor47.pack()
            if "KS" in msg:
                imname = "cartas/KS.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor48=tkinter.Label(top, image=im2, bd=10)
                valor48.pack()
            if "QC" in msg:
                imname = "cartas/QC.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor49=tkinter.Label(top, image=im2, bd=10)
                valor49.pack()
            if "QD" in msg:
                imname = "cartas/QD.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor50=tkinter.Label(top, image=im2, bd=10)
                valor50.pack()
            if "QH" in msg:
                imname = "cartas/QH.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor51=tkinter.Label(top, image=im2, bd=10)
                valor51.pack()
            if "QS" in msg:
                imname = "cartas/QS.png"
                im1 = Image.open(imname).convert("1")
                size = (im1.width // 8, im1.height // 8)
                im1 = ImageTk.BitmapImage(im1.resize(size))
                im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                valor52=tkinter.Label(top, image=im2, bd=10)
                valor52.pack()
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