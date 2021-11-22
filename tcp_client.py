import socket
from diffie_hellman import generate_q, generate_a, generate_public_key, generate_symmetric_key


def client(host='localhost', port=8082):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server

    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    options = {
        1: generate_q,
        2: generate_a,
        3: generate_public_key,
        4: generate_symmetric_key,
    }

    try:
        while True:
            # Send data
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
                sock.sendall(message.encode('utf-8'))

            if option_input == 6:
                data = sock.recv(2048)
                print("Received: %s" % data)

            if option_input == 7:
                break

    except socket.error as e:
        print("Socket error: %s" % str(e))
    except Exception as e:
        print("Other exception: %s" % str(e))
    finally:
        print("Closing connection to the server")
        sock.close()


client()
