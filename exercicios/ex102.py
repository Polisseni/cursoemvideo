def fatorial(num, show=False):
    """
    -> CALCULA O FATORIAL DE UM NÚMERO.
    :param num: o número a ser calculado.
    :param show: (opicional)Mostrar ou não a conta.
    :return: O valor do fatorial de um número num
    """
    f = 1
    for c in range (num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end= '')
            else:
                print(' = ', end='')
        f *= c
    return f



#PROGRAMA PRINCIAPL
print(fatorial(5, show=True)) #show=True PARA MOSTRAR A OPERAÇÃO TODA
help(fatorial)   #EXIBE A DOCKSTRING
