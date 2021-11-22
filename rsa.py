from random import randint
import sympy


def input_primes():
    p = int(input("Escolha p: \t"))
    q = int(input("Escolha q: \t"))
    return p, q


def input_e():
    e = int(input("Escolha e: \t"))
    return e


def generate_random_primes():
    p = sympy.randprime(0, 1000)
    q = sympy.randprime(0, 1000)
    return p, q


def calc_n(p, q):
    return p * q


def calc_m(p, q):
    return (p - 1) * (q - 1)


def calc_factorial(m):
    prime_numbers = list(sympy.sieve.primerange(0, 1000))
    result = m
    factorial = []

    while result != 1:
        for num in prime_numbers:
            if result % num == 0:
                factorial.append(num)
                result = result / num
                break

    return set(factorial)


def calc_e(m):
    factorial = calc_factorial(m)
    generate_random = True
    result = 0

    while generate_random:
        result = randint(1, m)

        for num in factorial:
            if result % num == 0:
                break
            generate_random = False

    return result


def calc_d(e, m):
    print(e, m)
    for num in range(1, m):
        if (e * num) % m == 1:
            return num
    return None


def generate_keys():
    p, q = generate_random_primes()  # input_primes()
    n = calc_n(p, q)
    m = calc_m(p, q)
    e = calc_e(m)  # input_e()
    d = calc_d(e, m)

    pu_key = (e, n)
    pr_key = (d, n)

    return pu_key, pr_key


def cipher_char(char, pu_key):
    ciphered_char = (char ** pu_key[0]) % pu_key[1]
    return ciphered_char


def cipher_message(message, pu_key):
    ciphered_chars = [chr(cipher_char(ord(char), pu_key)) for char in message]
    ciphered_message = ''.join(ciphered_chars)
    return ciphered_message


def decipher_char(char, pr_key):
    deciphered_char = (char ** pr_key[0]) % pr_key[1]
    return deciphered_char


def decipher_message(ciphered_message, pr_key):
    deciphered_chars = [chr(decipher_char(ord(char), pr_key)) for char in ciphered_message]
    deciphered_message = ''.join(deciphered_chars)
    return deciphered_message


def generate_rsa_keys():
    public_key, private_key = generate_keys()

    print(public_key)
    print(private_key)

    with open(f"public_key", "w") as file:
        file.write(str(public_key))

    with open(f"private_key", "w") as file:
        file.write(str(private_key))


def cipher_rsa_message():
    input_message = input("Escolha a mensagem: \t")
    public_key_e = int(input("Digite a chave publica e: \t"))
    public_key_n = int(input("Digite a chave privada n: \t"))
    public_key = (public_key_e, public_key_n)
    c_message = cipher_message(input_message, pu_key=public_key)

    with open(f"mensagem-encriptada", "w") as file:
        file.write(c_message)

    return c_message


def decipher_rsa_message():
    input_message = input("Escolha a mensagem: \t")
    private_key_e = int(input("Digite a chave privada d: \t"))
    private_key_n = int(input("Digite a chave privada n: \t"))
    private_key = (private_key_e, private_key_n)
    d_message = decipher_message(input_message, pr_key=private_key)

    with open(f"mensagem-decriptada", "w") as file:
        file.write(d_message)

    return d_message


option_input = int(input("Escolha a ação desejada: \n"
                         "1 - Gerar chaves RSA \n"
                         "2 - Encriptar mensagem \n"
                         "3 - Decriptar mensagem \n"))

options = {
    1: generate_rsa_keys,
    2: cipher_rsa_message,
    3: decipher_rsa_message,
}

result = options.get(option_input)()
print(result)
