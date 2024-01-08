from socket import *

servidor ="127.0.0.1" #localhost
porta=43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    conexao, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(conexao.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Ola cliente'
        conexao.send(msg_enviada)
        break
    conexao.close()

# não muita interatividade enquanto não tiver outras aplicações clientes interagindo com ela ;)