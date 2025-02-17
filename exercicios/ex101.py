def voto (ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'{idade} anos é MENOR de idade, NÃO vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'{idade} anos o VOTO é OPICIONAL'
    else:
        return f'{idade} anos o Voto é OBRIGATÓRIO!!'


#PROGRAMA PRINCIPAL
nasc = int(input('Digite o ano em que você nasceu: '))
print(voto(nasc))
