import socket
from diffie_hellman import generate_q, generate_a, generate_public_key, generate_symmetric_key


def server(host='localhost', port=8082):
    data_payload = 2048  # The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5)

    print("Waiting to receive message from client")
    client, address = sock.accept()

    options = {
        1: generate_q,
        2: generate_a,
        3: generate_public_key,
        4: generate_symmetric_key,
    }

    while True:
        option_input = int(input("Escolha a ação desejada: \n"
                                 "1 - Gerar q \n"
                                 "2 - Gerar a \n"
                                 "3 - Gerar chave pública \n"
                                 "4 - Gerar chave simétrica \n"
                                 "5 - Enviar mensagem \n"
                                 "6 - Receber mensagem \n"
                                 "7 - Sair \n"))

        if option_input in options.keys():
            result = options.get(option_input)()
            print(result)

        if option_input == 5:
            message = input("Digite a mensagem a ser enviada: \t")
            print("Sending %s" % message)
            client.sendall(message.encode('utf-8'))

        if option_input == 6:
            data = client.recv(2048)
            print("Received: %s" % data)

        if option_input == 7:
            client.close()
            break


server()
