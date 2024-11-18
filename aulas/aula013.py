#for c in range (0, 6):
#    print('OI')   VAI IMPRIMIR "OI" 6X
#print('FIM')


#for c in range(1, 7):
#    print(c)   VAI IMPRIMIR DE 1 ATÉ 6
#print('FIM')


for c in range (7, 0, -1):   # -1 REPRESENTA A ITERAÇÃO PARA A CONTAGEM REGRESSIVA
    print(c)
print('FIM')


for c in range (0, 7, 2):   # 2 REPRESENTA A INTERAÇÃO PARA "PULAR DE 2 EM DOIS"
    print(c)
print('FIM')


#n = int(input('Digite um valor: '))
#for c in range (0, n+1):
#    print(c)
#print('FIM')


i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range (i, f, p):
    print(c)
print('FIM')


for c in range (0, 3):
    n = int(input('DIGITE UM VALOR: '))  # COLOCANDO VARIÁVEL ANINHADA, O PROCESSO SE REPETIRÁ 3X DADO O INTERVALO DE 0 A 3
print('FIM')


s = 0
for c in range (0, 4):
    n = int(input('DIGITE UM VALOR: '))  # VAI SOMAR OS VALORES DIGITADOS
    s += n
print(f'O somatório de todos os valores deu {s}')
print('FIM')