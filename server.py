from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from utils import Hall, Room, Player
import utils
import random
import time

global cartas, contador, hall, users, room

cartas = [
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

contador = 0
hall = ["Sala de prueba", "sala", "salita"]
#hall = []
users = ["ive"]
room = []
print(' '.join(cartas))
random.shuffle(cartas)
print("REVOLVIENDO CARTAS...",cartas)

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s Se ha conectado exitosamente." % client_address)
        client.send(bytes("¡Bienvenido al juego! Por favor, ingrese su nombre de usuario", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
    
def handle_client(client): 
    username = client.recv(BUFSIZ).decode("utf8")
    while(username in users): 
        client.send(bytes("El nombre de usuario ya está en uso, por favor utiliza uno diferente", "utf8"))
        username = client.recv(BUFSIZ).decode("utf8")
    Thread(target=handle_hall, args=(client,username)).start()

def handle_hall(client, username): 
    client.send(bytes("Para empezar a jugar debes unirte a una sala", "utf8"))
    while(len(hall) == 0): 
        hall_msg = "Oops! No hay salas disponibles, puedes crear la tuya utilizando <crear> nombre_sala"
        client.send(bytes(hall_msg, "utf8"))
        nueva = client.recv(BUFSIZ).decode("utf8")
        if (nueva.split()[0] == "crear"): 
            if(nueva.split()[0] not in hall): 
                hall.append(nueva.split()[1])
            else: 
                client.send(bytes("La sala que estás intentando crear ya existe", "utf8"))
                client.send(bytes("Si deseas unirte a la sala utiliza el comando <unirse> nombre_sala", "utf8"))

    client.send(bytes("Las salas disponibles  son \r\n", "utf8")) 
    for room in hall:
        roomy = "- " + room
        client.send(bytes(roomy, "utf8"))
    Thread(target=handle_room, args=(client,username)).start()

def handle_room(client, username): 
    msg2 = "Únete a una sala utilizando <unirse> nombre_sala"
    client.send(bytes(msg2, "utf8"))
    room = []
    flag = True
    while(flag == True):
        join = client.recv(BUFSIZ).decode("utf8")
        if (join.split()[0] == "unirse"): 
            if not room: 
                chsn_room = join.split()[1]
                #room[0] = chsn_room
                flag = False
            else: 
                """s
                client.send(bytes("Ya estas unido a una sala, seguro que quieres cambiar? si/no", "utf8"))
                
                op = client.recv(BUFSIZ).decode("utf8")
                if (op == "si"): 
                    chsn_room = join.split()[1]
                    room[0] = chsn_room
                else: 
                    chsn_room = room[0]
                """
                flag = False
        else: 
            client.send(bytes("Comando no valido", "utf8"))
            

    print("lo que eligio fue ", chsn_room)
    Thread(target=handle_game, args=(client,username, chsn_room)).start()

def handle_game(client, username, room):  
    global contador
    print("Sala", room)
    print("Numero de clientes ",contador) 
    print("Se ha conectado el usuario: ", username)
    sala_msg = "Bienvenid@ a la sala %s" % room
    client.send(bytes(sala_msg, "utf8"))
    welcome = "¡Hola %s! Si desea salir escriba {quit} si desea comenzar el juego escrita {start}" % username
    client.send(bytes(welcome, "utf8"))
    if (contador <= contador):
        contador = contador + 1
        print(contador)
    msg = "¡%s Se ha unido al juego!" % username
    broadcast(bytes(msg, "utf8"))
    clients[client] = username
    while True:
        print(contador)
        jugador1 = cartas[0:4]
        jugador1 = (' '.join(jugador1))
        jugador2 = cartas[4:8]
        jugador2 = (' '.join(jugador2))
        jugador3 = cartas[8:12]
        jugador3 = (' '.join(jugador3))
        if contador == 1:
            client.send(bytes(jugador1,"utf8" ))
            print("jugador1", jugador1)
            print("necesitas mas jugadores")
        if contador == 2:
            print("jugador2", jugador2)
            client.send(bytes(jugador2,"utf8" ))
        if contador == 3:
            print("jugador3", jugador3)
            client.send(bytes(jugador3,"utf8" ))
            #me da pereza hacer mas 
        msg = client.recv(BUFSIZ)
        print("mensaje recibidio",msg, "de:", username)
        if msg != bytes("quit", "utf8"):
            broadcast(msg, username+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s se ha retirado del juego" % username, "utf8"))
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

if __name__ == "__main__":
    #interfaz grafica del server comentado
    #CardShuffler().root.mainloop()
    SERVER.listen(5)
    print("Esperando jugadores...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()