from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range (1, 8):
    nasc = int(input(f'Escreva em que ano a {pessoa} pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor +=1
print(f'Ao todo tivemos {totmaior} pessoa(s) maior(es) de idade')
print(f'E tivemos {totmenor} pessoa(s) menor(es) de idade')

