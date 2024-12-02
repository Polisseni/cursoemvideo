n = c = 0
while True:
    n = int(input('Digite um número inteiro para saber sua tabuada: '))
    print('-=' * 20)
    if n < 0:
        break
    for c in range (0,11):
        print(f'{n} x {c} = {n*c}')
    print('-=' * 20)
print('\033[1;34mPROGAMA DE TABUADA ENCERRADO!! MUITO OBRIGADO, VOLTE SEMPRE\033[m')
