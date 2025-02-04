temp = list()
princ = list()
pesomaior = pesomenor = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if len(princ) == 0: #SE NÃO TIVER NINGUÉM CADASTRADO AINDA:
        pesomaior = pesomenor = temp[1] #GUARDAR NO PESO
    else:
        if temp[1] > pesomaior:
            pesomaior = temp[1]
        if temp[1] < pesomenor:
            pesomenor = temp[1]
    princ.append(temp[:])
    temp.clear() #CLEAR PARA MOSTRAR APENAS UMA VEZ CADA DADO DA LISTA PRINCIPAL
    resp = str(input('Quer CONTINUAR?[S/N]: ')).strip().upper()
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi de {pesomaior} KG, o peso de ', end='')
for p in princ:
    if p[1] == pesomaior:
        print(f'{p[0]}', end='')
print(f'\nO menor peso foi de {pesomenor} KG, o peso de ', end='')
for p in princ:
    if p[1] == pesomenor:
        print(f'{p[0]}', end='')
print()
