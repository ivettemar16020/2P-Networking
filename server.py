from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from utils import Hall, Room, Player
import utils
import random
import time

global cartas, contador, hall, room

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
room = []
client_dir = []
users = []
turnos = [1,2,3,4]
index = 0
print(' '.join(cartas))
random.shuffle(cartas)
print("REVOLVIENDO CARTAS... ", cartas)


def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s Se ha conectado exitosamente." % client_address)
        client.send(bytes("¡Bienvenido al juego! Por favor, ingrese su nombre de usuario", "utf8"))
        addresses[client] = client_address
        client_dir.append(client_address)
        print(client_dir)
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    username = client.recv(BUFSIZ).decode("utf8")
    while username in users:
        client.send(bytes("El nombre de usuario ya está en uso, por favor utiliza uno diferente", "utf8"))
        username = client.recv(BUFSIZ).decode("utf8")
    users.append(username)
    print(users)
    Thread(target=handle_hall, args=(client,username)).start()
    return users


def handle_hall(client, username): 
    client.send(bytes("Para empezar a jugar debes unirte a una sala", "utf8"))
    while len(hall) == 0:
        hall_msg = "Oops! No hay salas disponibles, puedes crear la tuya utilizando <crear> nombre_sala"
        client.send(bytes(hall_msg, "utf8"))
        nueva = client.recv(BUFSIZ).decode("utf8")
        if nueva.split()[0] == "crear":
            if nueva.split()[0] not in hall:
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
    while flag == True:
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
    global users
    global client_dir
    global cartas1
    global cartas2
    global cartas3
    global messagedecode
    jugador1 = False
    jugador2 = False
    jugador3 = False
    jugador4 = False
    usuario = "user:" + users[0]
    client.send(bytes(usuario, "utf8"))
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
        n = 4
        if contador == 1 and jugador1 == False:
            if jugador4 == False:
                print(users)
                print(client_dir)
                jugador1 = cartas[0:4]
                jugador1 = (' '.join(jugador1))
                jugador1 = "cards :" + jugador1
                message1 = users[0] + " " + jugador1
                client.sendto(bytes(message1, "utf8"), client_dir[0])
                client.sendto(bytes("\nPrueba solo para P1", "utf8"), client_dir[0])
                cartas1 = cartas[n:]
                print(cartas1)
                print("jugador1", jugador1)
                print("necesitas mas jugadores")
                jugador1 = True
                jugador4 = False
        if contador == 2 and jugador2 == False:
            if jugador1 == False:
                print(client_dir)
                jugador2 = cartas[4:8]
                jugador2 = (' '.join(jugador2))
                jugador2 = "cards :" + jugador2
                print("jugador2", jugador2)
                message2 = users[1] + " " + jugador2
                client.sendto(bytes(message2, "utf8"), client_dir[1])
                client.sendto(bytes("\nPrueba solo para P2", "utf8"), client_dir[1])
                cartas2 = cartas1[n:]
                print(cartas2)
                jugador2 = True
                jugador1 = False
        if contador == 3 and jugador3 == False:
            if jugador2 == False and jugador1 == False:
                jugador3 = cartas[8:12]
                jugador3 = (' '.join(jugador3))
                jugador3 = "cards :" + jugador3
                print("jugador3", jugador3)
                message3 = users[2] + " " + jugador3
                client.sendto(bytes(message3, "utf8"), client_dir[2])
                client.sendto(bytes("\nPrueba solo para P3", "utf8"), client_dir[2])
                cartas3 = cartas2[n:]
                print(cartas3)
                jugador3 = True
                jugador2 = False
                jugador1 = False
        if contador == 4 and jugador4 == False:
            if jugador3 == False and jugador2 == False and jugador1 == False:
                jugador4 = cartas[12:16]
                jugador4 = (' '.join(jugador4))
                jugador4 = "cards :" + jugador4
                print("jugador4", jugador4)
                message4 = users[3] + " " + jugador4
                client.sendto(bytes(message4, "utf8"), client_dir[3])
                client.sendto(bytes("\nPrueba solo para P4", "utf8"), client_dir[3])
                cartas4 = cartas3[n:]
                print(cartas4)
                print("listo para jugar")
                jugador4 = True
                jugador3 = False
                jugador2 = False
                jugador1 = False
        if contador == 5:
            print("SALA LLENA ESCOGE OTRA SALA")
        msg = client.recv(BUFSIZ)
        if bytes("cartapasar:", "utf8") in msg:
            print("RECIBIDO EL CODIGO cartapasar TEST!")
            messagedecode = msg.decode("utf-8")
            messagedecode = messagedecode.replace('cartapasar:', '') 
            messagedecode = messagedecode.replace(" ", "")
            print("CARTA", messagedecode)
            messagedecode = "turno1"+ messagedecode
            print("CARTA RECIBIDA", messagedecode, username)
            #finduser = users.index(username)
            #print("INDICE DEL USER", finduser)
            #print("DEBUGEANDO", client_dir)
            #print("DEBUGEANDO2", client_dir[0] )
            #print("DEBUGEANDO2a", client_dir[finduser] )
            #print("DEBUGEANDO3", client_dir[1] )
            #finduser = finduser + 1
            #print("DEBUGEANDO4a", client_dir[finduser])
            #buscar porque solo se envia a si mismo
            # client.sendto(bytes(messagedecode, "utf8"), client_dir[finduser])
            #client.sendto(bytes(messagedecode, "utf8"), client_dir[finduser-1])
            #msg.replace('carta pasada b'cartapasar:', '')
            #client.sendto(bytes(msg, "utf8"))
        if msg == bytes("recibiendo", "utf8"):
            global index
            lenght = len(turnos)
            turno = turnos[index]
            index = (index + 1) % lenght
            avisarturno = "Turno del Usuario:" + str(turno)
            client.sendto(bytes(messagedecode, "utf8"), client_dir[0])
            broadcast(bytes(avisarturno, "utf8"))
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

def send_to():
    global client_dir
    for sock in clients:
        print(client_dir[0])
        print(client_dir[1])
        sock.sendto(bytes("Mensaje para USUARIO No.1 SOLAMENTE!", "utf8"), client_dir[0])

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
