from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
import tkinter.font as tkFont
from cards import *
import random
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import random
deck = generate_deck()
# inicializar deck
sampled_deck = deck
card_images = {}

contador = 0

# Carga todas las imagenes del diccionario
for card in deck:
    image = Image.open("cartas/" + card.getNameForImage() + ".png")
    image = image.resize((70, 100), Image.ANTIALIAS)
    card_images.update({card.getNameForImage() : image})

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s Se a conectado." % client_address)
        client.send(bytes("Bienvenido al juego! Ingrese su nombre de usuario", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
        

def handle_client(client):  
    global contador
    print("numero de clientes",contador) 
    name = client.recv(BUFSIZ).decode("utf8")
    print("usuario conectado", name)
    welcome = 'Bienvenido %s! Si desea salir escriba {quit} si desea comenzar el juego escrita {start}' % name
    client.send(bytes(welcome, "utf8"))
    if (contador <= contador):
        contador = contador + 1
        print(contador)
    msg = "%s Se a unido al juego!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        listo_para_jugar = input("Presiona j para determinar que ya estas listo para jugar: ")
        if listo_para_jugar == "j":
            cartas = ["2C", "2D", "2H", "2S", "3C", "3D", "3H", "3S", "4C", "4D", "4H", "4S", "5C", "5D", "5H", "5S", "6C", "6D", "6H", "6S", "7C", "7D", "7H", "7S", "8C", "8D", "8H", "8S", "9C", "9D", "9H", "9S", "10C", "10D", "10H", "10S", "AC", "AD","AH", "AS", "JC", "JD", "JH", "JS", "KC", "KD", "KH", "KS", "QC", "QD", "QH", "QS"]
            print(' '.join(cartas))
            random.shuffle(cartas)
            print("REVOLVIENDO CARTAS...",cartas)
            print(contador)
            if contador == 1:
                print("necesitas mas jugadores")
            if contador == 2:
                jugador1 = cartas[0:4]
                jugador1 = (' '.join(jugador1))
                print("jugador1", jugador1)
                client.send(bytes(jugador1,"utf8" ))
                jugador2 = cartas[4:8]
                jugador2 = (' '.join(jugador2))
                print("jugador2", jugador2)
                client.send(bytes(jugador1,"utf8" ))
            if contador == 3:
                jugador1 = cartas[0:4]
                print("jugador1", jugador1)
                jugador2 = cartas[4:8]
                print("jugador2", jugador2)
                jugador3 = cartas[8:12]
                print("jugador3", jugador3)
            #me da pereza hacer mas 
        msg = client.recv(BUFSIZ)
        print("mensaje recibidio",msg, "de:", name)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s a salido del juego." % name, "utf8"))
            break

def broadcast(msg, prefix=""):  
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)
clients = {}
addresses = {}
#HOST = '192.168.1.17' con el ifconfig de mi computadora
HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
#clase para interfaz grafica actualmente no se esta utilizando
class CardShuffler:
    root = tk.Tk()
    sampled_deck = deck
    card_frame = None
    card_number_spinner = None
    show_cards = True
    main_frame = None
    cmb_card_value = None
    cmb_card_symbol = None
    picking_counter_label = None
    picking_counter_val_label = None

    def __init__(self):
    
        self.root.resizable(False, False) 
        main_menu_fonts = tkFont.Font(size=25, family="Arial Bold")
        self.master = self.root
        self.root.title("Cucharita")
        self.frame = tk.Frame(self.master, width=1280, height=720, background="#eee")
        start_button = tk.Button(fg="#fff", font=main_menu_fonts, borderwidth = 0, text = 'START', width = 20, bg="#222", command = lambda: self.start_game(self.frame), padx = 5, pady = 5)
        start_button.place(in_=self.frame, anchor="c", relx=.5, rely=.4)
        self.frame.pack(fill="both", expand=True)
        

    def start_game(self, frame):
        self.frame.destroy()
        self.main_frame = tk.Frame(self.master, width=1280, height=720, background="#ccc")
        self.card_frame = tk.Frame(self.main_frame, height = 800, width = 900, bg = "#eee", borderwidth=2)
        self.display_card_images(self.card_frame, deck, self.show_cards)
        pick_random_card_btn = tk.Button(text="Pick Random Card",width = 29, command=self.pick_random_card);
        pick_random_card_btn.place(in_=self.main_frame, anchor="c", x=1078, y=200)
        main_menu_fonts = tkFont.Font(size=15, family="Arial Bold")
        self.picking_counter_val_label = tk.Label(text="", font=main_menu_fonts, bg="#ccc", fg="#222")   
        self.picking_counter_val_label.place(in_=self.main_frame, anchor="c", x=1185, y=620)
        self.cmb_card_value = ttk.Combobox(state='readonly', width = 10, values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.cmb_card_value.bind("<<ComboboxSelected>>", self.cmb_changed_event)
        self.cmb_card_value.grid(column=0, row=1)
        self.cmb_card_value.current(1)
        self.cmb_card_value.place(in_=self.main_frame, anchor="c", x=1010, y=460)
        self.cmb_card_symbol = ttk.Combobox(state='readonly', width = 10, values=["Heart", "Diamond", "Spade", "Club"])
        self.cmb_card_symbol.bind("<<ComboboxSelected>>", self.cmb_changed_event)
        self.cmb_card_symbol.grid(column=0, row=1)
        self.cmb_card_symbol.current(1)
        self.cmb_card_symbol.place(in_=self.main_frame, anchor="c", x=1145, y=460)
        spinner_def_value = tk.StringVar(self.root)
        spinner_def_value.set("52")
        self.card_frame.pack(side="top", anchor="w")
        self.main_frame.pack()
        self.main_frame.pack_propagate(0)

    def cmb_changed_event(self, eventObject):
        card_name = self.get_card_name_from_combobox()
        selected_card = None
        for card in deck:
            if card.getNameForImage() == card_name:
                selected_card = card
                break
        self.display_random_card(selected_card)

    def get_card_name_from_combobox(self):
        card_value = self.cmb_card_value.get()
        card_symbol = self.cmb_card_symbol.get()
        full_card_name = card_value + card_symbol
        card_name = ""
        if full_card_name[1].isdigit():
            card_name = full_card_name[0:3]
        else:
            card_name = full_card_name[0:2]
        return card_name    

    def display_random_card(self, card):
        card = Image.open("cartas/" + card.getNameForImage() + ".png")
        card = card.resize((110, 160), Image.ANTIALIAS)
        card_image = ImageTk.PhotoImage(card)
        card_image_container = tk.Label(image=card_image, borderwidth=0, bg="#ccc")
        card_image_container.image = card_image
        card_image_container.place(in_=self.main_frame, x=1020, y=230)
    
    def pick_random_card(self):
        random_card = random.choice(self.sampled_deck)
        self.display_random_card(random_card)
    def display_card_images(self, frame, deck, showCards):
        x_add = 10
        y_add = 10
        y_counter = 0
        for card in deck:
            y_counter += 1
            if showCards == True:
                card_image = ImageTk.PhotoImage(card_images[card.getNameForImage()])
            else:
                card_image = ImageTk.PhotoImage(default_card_image)

            card_image_container = tk.Label(image=card_image)
            card_image_container.image = card_image
            card_image_container.place(in_=frame, x=x_add % 800, y=y_add)
            x_add += 80
            y_add += (110 if y_counter % 10 == 0 else 0)
        
if __name__ == "__main__":
    #interfaz grafica del server comentado
    #CardShuffler().root.mainloop()
    SERVER.listen(5)
    print("Esperando jugadores...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()