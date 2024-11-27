cont = 0
num = 0
soma = 0
num = int(input('Digite um número inteiro qualquer [999 PARA PARAR]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro qualquer [999 PARA PARAR]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
print('ACABOU')