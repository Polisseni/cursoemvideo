num = int(input('Digite um número: '))
total = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[0;33m ', end = '')
        total += 1
    else:
        print('\033[0;31m ', end = '')
    print(f'{c}', end = '')
print(f'\n\033[0;34mO número {num} foi dividido {total} vezes\033[m')
if total == 2:
    print('\033[0;34mE por isso ele é PRIMO !!!\033[m')