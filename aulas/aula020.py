def soma (a, b):
    print(f'a = {a} e b = {b}')
    s = a + b
    print(f'A soma dos elementos vale: {s}')


#PROGRAMA PRINCIPAL
soma (b=4, a=5)
soma (7, 3)  #SE NÃO EXPLICITAR O PRIMEIRO VALOR VAI PARA "A' E O SEGUNDO VALOR PARA "B"
#soma(3, 9, 5) PRECISA SEGUIR A DEFINIÇÃO INICIAL, MAS...

def contador (* num):
    tam = len(num)
    print(f'Recebi os valores {num} totalizando {tam} elementos!', end='')
    print('FIM!')  #VÁRIOS PARÂMETROS, PEGAR TODOS E JOGAR DENTRO DE NUM

contador(1, 4, 8)
contador(0, 8)
contador(1, 2, 4, 9)

def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 6, 8, 9]  #LEMBRAR DE USAR LISTAS E NÃO TUPLAS
dobra(valores)
print(valores)

def soma (*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma (2, 5)
soma (2, 9, 4)
