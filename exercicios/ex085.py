num = [[], []]
valor = 0
for c in range (1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()  #ORDENAR AS LISTAS UMA DE CADA VEZ
num[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')
