import socket

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5432        # Porta usada pelo servidor

# Cria um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta-se ao servidor
    s.connect((HOST, PORT))
    # Envia uma mensagem
    s.sendall(b'Ola , servidor TCP!')
    # Recebe a resposta do servidor
    data = s.recv(1024)

print('Mensagem recebida do servidor:', data.decode())
