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
                    print(*miscartas, sep = ", ")
                    imname = "cartas/2C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor3=tkinter.Label(top, image=im2, bd=10)
                    valor3.pack()

                if "2D" in msg:
                    miscartas.append('2D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/2D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor3=tkinter.Label(top, image=im2, bd=10)
                    valor3.pack()
                if "2H" in msg:
                    miscartas.append('2H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/2H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor4=tkinter.Label(top, image=im2, bd=10)
                    valor4.pack()

                if "2S" in msg:
                    miscartas.append('2S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/2S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor5=tkinter.Label(top, image=im2, bd=10)
                    valor5.pack()

                if "3C" in msg:
                    miscartas.append('3C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/3C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor6=tkinter.Label(top, image=im2, bd=10)
                    valor6.pack()

                if "3D" in msg:
                    miscartas.append('3D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/3D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor7=tkinter.Label(top, image=im2, bd=10)
                    valor7.pack()

                if "3H" in msg:
                    miscartas.append('3H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/3H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor8=tkinter.Label(top, image=im2, bd=10)
                    valor8.pack()

                if "3S" in msg:
                    miscartas.append('3S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/3S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor9=tkinter.Label(top, image=im2, bd=10)
                    valor9.pack()

                if "4C" in msg:
                    miscartas.append('4C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/4C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor10=tkinter.Label(top, image=im2, bd=10)
                    valor10.pack()

                if "4D" in msg:
                    miscartas.append('4D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/4D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor11=tkinter.Label(top, image=im2, bd=10)
                    valor11.pack()

                if "4H" in msg:
                    miscartas.append('4H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/4H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor12=tkinter.Label(top, image=im2, bd=10)
                    valor12.pack()

                if "4S" in msg:
                    miscartas.append('4S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/4S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor13=tkinter.Label(top, image=im2, bd=10)
                    valor13.pack()

                if "5C" in msg:
                    miscartas.append('5C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/5C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor14=tkinter.Label(top, image=im2, bd=10)
                    valor14.pack()
                if "5D" in msg:
                    miscartas.append('5D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/5D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor15=tkinter.Label(top, image=im2, bd=10)
                    valor15.pack()

                if "5H" in msg:
                    miscartas.append('5H')
                    print(*miscartas, sep = ", ")
                    iname = "cartas/5H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor16=tkinter.Label(top, image=im2, bd=10)
                    valor16.pack()

                if "5S" in msg:
                    miscartas.append('5S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/5S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor17=tkinter.Label(top, image=im2, bd=10)
                    valor17.pack()
                if "6C" in msg:
                    miscartas.append('6C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/6C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor18=tkinter.Label(top, image=im2, bd=10)
                    valor18.pack()

                if "6D" in msg:
                    miscartas.append('6D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/6D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor19=tkinter.Label(top, image=im2, bd=10)
                    valor19.pack()

                if "6H" in msg:
                    miscartas.append('6H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/6H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor20=tkinter.Label(top, image=im2, bd=10)
                    valor20.pack()

                if "6S" in msg:
                    miscartas.append('6S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/6S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor21=tkinter.Label(top, image=im2, bd=10)
                    valor21.pack()

                if "7C" in msg:
                    miscartas.append('7C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/7C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor22=tkinter.Label(top, image=im2, bd=10)
                    valor22.pack()

                if "7D" in msg:
                    miscartas.append('7D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/7D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor23=tkinter.Label(top, image=im2, bd=10)
                    valor23.pack()

                if "7H" in msg:
                    miscartas.append('7H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/7H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor24=tkinter.Label(top, image=im2, bd=10)
                    valor24.pack()

                if "7S" in msg:
                    miscartas.append('7S')
                    print(*miscartas, sep = ", ")
                    iname = "cartas/7S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor25=tkinter.Label(top, image=im2, bd=10)
                    valor25.pack()

                if "8C" in msg:
                    miscartas.append('8C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/8C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor26=tkinter.Label(top, image=im2, bd=10)
                    valor26.pack()

                if "8D" in msg:
                    miscartas.append('8D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/8D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor27=tkinter.Label(top, image=im2, bd=10)
                    valor27.pack()

                if "8H" in msg:
                    miscartas.append('8H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/8H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor28=tkinter.Label(top, image=im2, bd=10)
                    valor28.pack()

                if "8S" in msg:
                    miscartas.append('8S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/8S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor29=tkinter.Label(top, image=im2, bd=10)
                    valor29.pack()

                if "9C" in msg:
                    miscartas.append('9C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/9C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor30=tkinter.Label(top, image=im2, bd=10)
                    valor30.pack()

                if "9D" in msg:
                    miscartas.append('9D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/9D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor31=tkinter.Label(top, image=im2, bd=10)
                    valor31.pack()

                if "9H" in msg:
                    miscartas.append('9H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/9H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor32=tkinter.Label(top, image=im2, bd=10)
                    valor32.pack()

                if "9S" in msg:
                    miscartas.append('9S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/9S.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor33=tkinter.Label(top, image=im2, bd=10)
                    valor33.pack()

                if "10C" in msg:
                    miscartas.append('10C')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/9C.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor34=tkinter.Label(top, image=im2, bd=10)
                    valor34.pack()

                if "10D" in msg:
                    miscartas.append('10D')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/10D.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor35=tkinter.Label(top, image=im2, bd=10)
                    valor35.pack()

                if "10H" in msg:
                    miscartas.append('10H')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/10H.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor36=tkinter.Label(top, image=im2, bd=10)
                    valor36.pack()

                if "10S" in msg:
                    miscartas.append('10S')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/AS.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor37=tkinter.Label(top, image=im2, bd=10)
                    valor37.pack()

                if "AC" in msg:
                    miscartas.append('AC')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/AC.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor38=tkinter.Label(top, image=im2, bd=10)
                    valor38.pack()

                if "AD" in msg:
                    miscartas.append('AC')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/AD.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor39=tkinter.Label(top, image=im2, bd=10)
                    valor39.pack()

                if "AH" in msg:
                    miscartas.append('AH')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/AH.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor40=tkinter.Label(top, image=im2, bd=10)
                    valor40.pack()

                if "AS" in msg:
                    miscartas.append('AS')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/AS.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor41=tkinter.Label(top, image=im2, bd=10)
                    valor41.pack()

                if "JC" in msg:
                    miscartas.append('JC')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/JC.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor42=tkinter.Label(top, image=im2, bd=10)
                    valor42.pack()

                if "JD" in msg:
                    miscartas.append('JD')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/JD.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor43=tkinter.Label(top, image=im2, bd=10)
                    valor43.pack()

                if "JH" in msg:
                    miscartas.append('JH')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/JH.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor43=tkinter.Label(top, image=im2, bd=10)
                    valor43.pack()

                if "JS" in msg:
                    miscartas.append('JS')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/JS.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor44=tkinter.Label(top, image=im2, bd=10)
                    valor44.pack()

                if "KC" in msg:
                    miscartas.append('KC')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/KC.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor45=tkinter.Label(top, image=im2, bd=10)
                    valor45.pack()

                if "KD" in msg:
                    miscartas.append('KD')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/KD.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor46=tkinter.Label(top, image=im2, bd=10)
                    valor46.pack()

                if "KH" in msg:
                    miscartas.append('KH')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/KH.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor47=tkinter.Label(top, image=im2, bd=10)
                    valor47.pack()

                if "KS" in msg:
                    miscartas.append('KS')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/KS.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor48=tkinter.Label(top, image=im2, bd=10)
                    valor48.pack()

                if "QC" in msg:
                    miscartas.append('QS')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/QC.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor49=tkinter.Label(top, image=im2, bd=10)
                    valor49.pack()

                if "QD" in msg:
                    miscartas.append('QD')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/QD.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor50=tkinter.Label(top, image=im2, bd=10)
                    valor50.pack()

                if "QH" in msg:
                    miscartas.append('QH')
                    print(*miscartas, sep = ", ")
                    imname = "cartas/QH.png"
                    im1 = Image.open(imname).convert("1")
                    size = (im1.width // 8, im1.height // 8)
                    im1 = ImageTk.BitmapImage(im1.resize(size))
                    im2 = ImageTk.PhotoImage(Image.open(imname).resize(size))
                    valor51=tkinter.Label(top, image=im2, bd=10)
                    valor51.pack()

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
                cartasactuales = (' '.join(miscartas[0]))
                cartasactuales1 = (' '.join(miscartas[1]))
                cartasactuales2 = (' '.join(miscartas[2]))
                cartasactuales3 = (' '.join(miscartas[3]))
                choices = {cartasactuales, cartasactuales1, cartasactuales2, cartasactuales3}
                tkvar = tkinter.StringVar()
                tkvar.set(cartasactuales) # set the default option
                popupMenu = OptionMenu(top, tkvar, *choices)
                popupMenu.pack()
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