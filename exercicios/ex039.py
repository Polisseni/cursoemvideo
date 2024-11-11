from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print(f'Você completa 18 anos em {atual} e deve se alistar no Serivço Militar')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Você náo completará 18 anos em {atual}, por isso não precisa se alistar esse ano, sómente em {saldo} anos')
    print(f'Deverá se alistar no ano de {ano}')
elif idade > 18:
#else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já completou 18 anos a {saldo} anos e precisa se alistar imediatamente')
    print(f'Seu ano de alistamento foi {ano}')

