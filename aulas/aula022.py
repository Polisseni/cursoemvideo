from Úteis import Números   #from uteis import fatorial, dobro (QUANDO IMPORTAR + DE UMA BIBLIOTECA, IMPORTAR A BIBLIOTECA TODA
#PROGRAMA PRINCIPAL
num = int(input('Digite um número: '))
fat = Números.fatorial (num)   #PARA NÃO USAR O "UTEIS." IMPORTAR A FUNÇÃO ESPECÍFICA
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {Números.dobro(num)}')


#AULA SOBRE UTILIZAÇÃO DE MÓDULOS E PACOTES EM PYTHON
'''def fatorial (n):
    f = 1
    for c in range (1, n + 1):
        f *= c
    return f


def dobro (n):
    return n * 2


def triplo (n):
    return n * 3
'''