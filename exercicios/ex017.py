#co = float(input('Digite o cateto oposto: '))
#ca = float(input('Digite o cateto adjacente: '))
#hip = (co**2+ca**2)**(1/2)
#print(f'O valor da hipotenusa do triângulo é: {hip}')

import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = math.hypot(co, ca)
print(f'O valor da hipotenusa é: {hip:.2f}')


from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = hypot(co, ca)
print(f'O valor da hipotenusa é: {hip:.2f}')

