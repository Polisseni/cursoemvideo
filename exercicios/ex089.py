ficha = list()
while True:
    nome = str(input('Nome: ')).strip().upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    res = str(input('Quer CONTINUAR ou não?[S/N]: '))
    if res in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:>10}{a[2]:>8.1f}')
while True:
    print('-='*30)
    opc = int(input('Mostrar notas de qual aluno? (999 INTERROMPE): '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('\033[1;34m<<<VOLTE SEMPRE>>>\033[m')
