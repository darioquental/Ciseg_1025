import socket,time

# criar a socket 
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# defenir ligaçao ao servidor
porta=12340
host="127.0.0.1"

#conectar ao servidor
clientSocket.connect((host,porta))

#enviar e receber mensagem

#Fechar a conecção
clientSocket.close()