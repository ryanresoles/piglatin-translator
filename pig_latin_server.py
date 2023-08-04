import socket
import threading

FORMAT = 'utf-8'
PORT = 3000
SERVER = socket.gethostbyname(socket.gethostname())

def isVowel(uinput):
    if uinput[0].lower()=='a' or uinput[0].lower()=='e' or uinput[0].lower()=='i' or uinput[0].lower()=='o' or uinput[0].lower()=='u':
        return uinput
    else:
        return isVowel(uinput[1:]+uinput[0])

def pig_latin(uinput):
    user_val = uinput
    arr_form = user_val.split(" ")

    message = ''
    for word in arr_form:
        temp = isVowel(word)
        message += temp+'ay '

    return message


def get_choice():
    choice = 0
    while True:
        choice = int(input("Receive another message? ([1]Yes/[0]No): "))
        if choice == 0 or choice == 1:
            break
        elif choice != 1:
            print("Invalid input.")
    
    return choice


# MAIN CODE #
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))

# This function handles the thread that handles the communication between the client and server
def handle_client(clientsocket, address):
    print(f"[CONNECTED] Connection from {address} has been established!")

    connected = True
    while connected:
        msg_length = clientsocket.recv(64).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = clientsocket.recv(msg_length).decode(FORMAT)

            pig_latin_message = pig_latin(msg)
            print(f"{address} Received: {msg} | Translation: {pig_latin_message}")
            clientsocket.send(pig_latin_message.encode(FORMAT))
            
            choice = get_choice()
            if choice == 0:
                connected = False
            
            

    clientsocket.close()

# Starts the server
# This function handles the connection between the client and server using threads
# Each thread handles a different connection
def start():
    s.listen(5)
    print(f"[LISTENING] Server is listening on {SERVER}...")

    while True:
        clientsocket, address = s.accept()
        thread = threading.Thread(target=handle_client, args=(clientsocket, address))
        thread.start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    
print("[STARTING] Server is starting...")
start()