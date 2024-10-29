import math

ângulo = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(ângulo))
print(f'O seno de {ângulo} é igual a: {sen:.2f}')
cos = math.cos(math.radians(ângulo))
print(f'O cosseno de {ângulo} é igual a: {cos:.2f}')
tan = math.tan(math.radians(ângulo))
print(f'A tangente de {ângulo} é igual a: {tan:.2f}')


from math import radians,sin,cos,tan


ângulo = float(input('Digite o ângulo desejado: '))
sen = sin(radians(ângulo))
print(f'O seno de {ângulo} é igual a: {sen:.2f}')
cos = cos(radians(ângulo))
print(f'O cosseno de {ângulo} é igual a: {cos:.2f}')
tan = tan(radians(ângulo))
print(f'A tangente de {ângulo} é igual a: {tan:.2f}')
