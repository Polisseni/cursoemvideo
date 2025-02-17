def factorial (num = 1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return f


f1 = factorial (5)
f2 = factorial (4)
f3 = factorial()
print(f'Os resulatods são: {f1}, {f2} e {f3}')


#------------------------------------------------------------------------------------------------------
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('\033[1;34mÉ PAR!!!\033[m')
else:
    print('\033[1;31mÉ ÍMPAR!!!\033[m')
