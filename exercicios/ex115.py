from time import sleep


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



def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;34m{c} - {item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua Opção: \033[m')
    return opc


#PROGRAMA PRINCIPAL
cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Muito Obrigado!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção VÁLIDA!\033[m')
    sleep(2)

