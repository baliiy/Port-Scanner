import socket as s
from sys import argv, exit


def port_scan(alvo, porta_inicial, porta_final):
    print(f'Scanning {alvo}')
    portas_abertas = []

    for porta in range(porta_inicial, porta_final + 1):
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((alvo, porta))
        sock.close()

        if resultado == 0:
            portas_abertas.append(porta)

    print(f'Portas abertas: {portas_abertas}')


if __name__ == '__main__':
    if len(argv) != 4:
        print('Modo de uso: python scan.py HOST PORTA_INICIAL PORTA_FINAL')
        print(argv)
        exit()

    alvo = argv[1]
    porta_inicial = int(argv[2])
    porta_final = int(argv[3])

    port_scan(alvo, porta_inicial, porta_final)