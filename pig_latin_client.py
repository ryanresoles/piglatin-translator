import socket

PORT = 3000
# gets server to connect to
ip_server = input("Enter IP Address: ")
SERVER = ip_server
FORMAT = "utf-8"
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


# This function handles the message sending of client to the server
def send(message):
    msg = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)
    print(f"Pig latin translation: {client.recv(2048).decode(FORMAT)}")


message = input("Enter message: ")
send(message)

connected = True
while connected: 
    choice = int(input("Continue? [1]Yes/[0]No: "))
    if choice==0:
        break
    elif choice == 1:
        message = input("Enter message: ")
        send(message)
    else:
        print("Invalid choice.")
        
