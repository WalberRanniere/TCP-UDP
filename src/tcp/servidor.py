import socket

HOST = "127.0.0.1"
PORT = 5432

# Cria um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Associa o socket ao endereço e à porta especificados
    s.bind((HOST, PORT))
    # Habilita o servidor para aceitar conexões
    s.listen()
    print("Servidor TCP esperando por conexões...")
    # Aceita uma conexão
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            # Recebe os dados do cliente
            data = conn.recv(1024)
            if not data:
                break
            # Imprime os dados recebidos
            print("Dados recebidos:", data.decode())
            # Envia uma mensagem de volta ao cliente
            conn.sendall(b'A conexao foi feita!')