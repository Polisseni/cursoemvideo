from datetime import date
ano = int(input('Qual ano deseja analisar? Digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
    print(f'O ano que estamos é {ano}')
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
