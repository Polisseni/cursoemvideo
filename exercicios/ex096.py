def area (larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')


#PROGRAMA PRINCIPAL
print('\033[1;36m CONTROLE DE TERRENOS\033[m ')
print('-'*20)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)
