from random import randint
import sympy


def generate_q():
    private_key = int(input("Digite a chave privada d: \t"))
    q = int(input("Digite q se já proposto ou 0 se não proposto: \t"))

    if q != 0:
        if q > private_key:
            return q
        else:
            return sympy.randprime(q, (q * 2))

    return sympy.randprime(private_key, (private_key * 2))


def generate_a():
    q = int(input("Digite o q: \t"))
    a = randint(1, q - 1)

    return a


def generate_number_pair():
    private_key = int(input("Digite a chave privada d: \t"))
    q = sympy.randprime(private_key, (private_key * 2))
    a = randint(1, q)
    return q, a


def generate_public_key():
    private_key = int(input("Digite a chave privada d: \t"))
    q = int(input("Digite o 'q': \t"))
    a = int(input("Digite o 'a': \t"))

    public_key = (a**private_key) % q

    return public_key


def generate_symmetric_key():
    public_key = int(input("Digite a chave pública: \t"))
    private_key = int(input("Digite a chave privada: \t"))
    q = int(input("Digite q: \t"))

    symmetric_key = (public_key**private_key) % q

    return symmetric_key


# option_input = int(input("Escolha a ação desejada: \n"
#                          "1 - Gerar q \n"
#                          "2 - Gerar a \n"
#                          "3 - Gerar chave pública \n"
#                          "4 - Gerar chave simétrica \n"))
#
# options = {
#     1: generate_q,
#     2: generate_a,
#     3: generate_public_key,
#     4: generate_symmetric_key,
# }
#
# result = options.get(option_input)()
#
# print(result)

