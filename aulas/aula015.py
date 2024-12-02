n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break   #comando BREAK para 'parar' o laço de repetição
    s += n      #quando o usuário digitar 999 o laço acaba e a soma é feita excluindo o número 999
print(f'A soma vale {s}')