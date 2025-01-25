num = [2,5,9,1]
num[2] = 3
#num[4] = 7 ERRO POR NÃO PODER ADICIONAR VALORES DESSA MANEIRA
num.append(7) # COMO SE ADICIONA UM ELEMENTO A UMA LISTA
num.sort() # COLOCANDO OS VALORES DA LISTA EM ORDEM
#num.sort(reverse=True) COLOCA OS VALORES EM ORDEM DE TRÁS PRA FRENTE
num.insert(2, 0) # NA POSIÇÃO 2 ADICIONOU O ZERO
#num.pop()  ELIMINA O ÚLTIMO VALOR DA LISTA
num.pop(2) # ELIMINA O ZERO DA LISTA
#num.remove(2) ELE VAI DO INÍCIO DA LISTA E REMOVE A PRIMEIRA OCORRÊNCIA '2' QUE TIVER
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

#--------------------------------------------------------------------------------------------

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} econtrei o valor {v}!')
print('Cheguei ao final da lista')

#---------------------------------------------------------------------------------------------

valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))  # PARA O USUÁRIO IR ADICIONANDO VALORES

for c, v in enumerate(valores):
    print(f'Na posição {c} econtrei o valor {v}!')
print('Cheguei ao final da lista')

