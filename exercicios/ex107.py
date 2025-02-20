from modex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é igual a {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')
print(f'Reduzindo 13% temos R${moeda.diminuir(p,13)}')

#MÓDULO ABAIXO
'''def metade (p):
    return p * 1/2


def dobro (p):
    return p * 2


def aumentar (p):
    return (p * 10/100) + p


def diminuir (p):
    return p - (p * 13/100)
'''
