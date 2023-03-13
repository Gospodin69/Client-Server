import socket as so

serverSocket = so.socket()

ip = "127.0.0.1"
port = 35491

serverSocket.bind((ip, port))

serverSocket.listen()

count = 0

while (True):
    (clientConnection, clientAddress) = serverSocket.accept()
    count = count + 1


    while(True):
        data = clientConnection.recv(1024)
        print(data)
        #First msg to client app
        msg1 = "Ako vidis ovu poruku server radi !!!"

        msg1Bytes = str.encode(msg1)

        clientConnection.send(msg1Bytes)
        #You have 999 msg to type if want more change that number
        for i in range(999):
            msg=input("Poruka od servera: ")
            msgBytes= str.encode(msg)
            clientConnection.send(msgBytes)






