import socket,time

#criar variavel para reter a socket
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#criar variavel para ip e porta
porta=12340
host="127.0.0.1"

# Bind (Vinculo) entre a porta ip e socket
serverSocket.bind((host,porta))

# start listen to conection
serverSocket.listen(1)
print(f"Servidor Ligado {host}:{porta}, aguarda conecçao")

# aceita conecçoes do cliente
clientsocket , endereçocliente = serverSocket.accept()
print(f"conecçao establecida {clientsocket} com endereço {endereçocliente}")

#açoes
time.sleep(200)

# Fecha a conexão com o client e o servidor
clientsocket.close()
serverSocket.close()