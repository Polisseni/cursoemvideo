soma = 0   #ACUMULADOR
cont = 0   #CONTADOR
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
        # CADA VEZ QUE O COMPUTADOR ACHAR UM NÚMERO DIVISÍVEL POR ZERO, ELE CONTA +1
        # TEM QUE ESTAR ANINHADO OU CONTARÁ OS 250 NÚMEROS IMPARES NO INTERVALO DE 1 A 500
print(f'A SOMA DE TODOS OS {cont} VALORES É {soma}')