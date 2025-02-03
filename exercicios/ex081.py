valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if res in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)  #PARA COLOCAR EM ORDEM DECRESCENTE
print(f'A ordem decrescente dos valores digitados na lista é {valores}')
if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
