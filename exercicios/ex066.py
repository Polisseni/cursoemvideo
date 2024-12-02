n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um número inteiro [999 PARA PARAR]: '))
    if n == 999:
        break
    c += 1   #depois do comando BREAK ou ele vai somar o 999 como +1 valor de contagem
    s += n
print(f'Foram digitados {c} valores e a soma entre eles é igual a {s}')
