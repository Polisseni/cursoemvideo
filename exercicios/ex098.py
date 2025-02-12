from time import sleep

def contador (i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p= 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep (2)

    if i < f:
        cont = i  #SE O INICIO É MENOR QUE O FINAL, O CONT COMEÇA COM INICIO
        while cont <= f:
            print(f'{cont}', end=' ', flush = True)
            sleep (0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush = True)
            sleep (0.5)
            cont -= p
    print('\033[1;34mFIM!\033[m')


#PROGRAMA PRINCIPAL
contador (1, 10, 1)
contador (10, 0, 2)
print('-=' * 20)
print('\033[1;34mAGORA É A SUA VEZ DE PERSONALIZAR A CONTAGEM!!\033[m')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
