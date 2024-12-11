lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata Frita')
print(sorted(lanche))  #COLOCANDO EM ORDEM ALFABÉTICA
#Tuplas são IMUTÁVEIS!!
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #PARA MOSTRAR A POSIÇÃO

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')  #FUNCIONA IGUAL AO DE CIMA

for comida in lanche:
    print(f'Eu comi {comida}')  #QUANDO NÃO PRECISA INDICAR A POSIÇÃO
print('Comi pra caramba!')

#----------------------------------------------------------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  #IRÁ JUNTAR AS DUAS TUPLAS, NÃO SOMAR E A TUPLA (C) É != B + A
print(c)
print(len(c))  #QUANTOS ELEMENTOS TEM EM (C)
print(c.count(5))  #QUANTAS VEZES O ELEMENTO '5' APARECE EM (C)
print(c.index(8))  #EM QUAL POSIÇÃO ESTÁ O ELEMENTO '8' EM (C)
print(c.index(2, 4))  #EK QUAL POSIÇÃO O ELEMENTO '2' ESTÁ EM (C) A PARTIR DA QUARTA POSIÇÃO

#---------------------------------------------------------------------------------------

pessoa = ('Gustavo', 39, 'M', 99.88)  #A TUPLA ACEITA ELEMENTOS DISTINTOS
#del pessoa    DEL PARA DELETAR A TUPLA
print(pessoa)