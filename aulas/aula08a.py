import math
num=int(input('Digite um número: '))
raiz=math.isqrt(num)
print(f'A raiz do número escolhido é: {math.ceil(raiz):.2f} ')


from math import sqrt,floor
num=int(input('Digite um número: '))
raiz=sqrt(num)
print(f'A raiz do número escolhido é {floor(raiz)}')