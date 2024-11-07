'''STYLE: 0(NONE)
          1(BOLD)
          4(UNDERLINE)
          7(NEGATIVR) '''

'''TEXT: 30(BRANCO)
         31(VERMELHO)
         32(VERDE)
         33(AMARELO)
         34(AZUL)
         35(ROXO)
         36(AZUL CLARO)
         37(CINZA) '''

'''BACK: 40(BRANCO)
         41(VERMELHO)
         42(VERDE)
         43(AMARELO)
         44(AZUL)
         45(ROXO)
         46(AZUL CLARO)
         47(CINZA)   '''

#\033[0;31;45m
print('\033[1;30;45mOlá, mundo!\033[m')
print('\033[7;30;mOlá, mundo!\033[m')

a = 3
b = 5
soma = a + b
print(f'A soma de \033[0;35m{a}\033[m com \033[0;31m{b}\033[m é igual a \033[0;32m{soma}\033[m')