from time import sleep


def ajuda (com):
    titulo(f'\033[1;34mACESSANDO O MANUAL DO COMANDO \'{com}\'\033[m')
    help(com)
    sleep(2)

def titulo (msg, cor=0):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    sleep(1)

#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('\033[1;35mSISTEMA DE AJUDA PYHELP\033[m')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('\033[1;31mATÉ LOGO!!\033[m')
