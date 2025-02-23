def leiaInt (msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro VÁLIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de DADOS interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def leiaFloat (msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real VÁLIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de DADOS interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


#PROGRAMA PRINCIPAL
n1 = leiaInt('Digite um valor INTEIRO: ')
n2 = leiaFloat(('Digite um valor REAL: '))
print(f'O valor digitado (INTEIRO) foi {n1} e o valor digitado REAL foi {n2}!')
