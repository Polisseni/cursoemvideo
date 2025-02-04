teste = list()
teste.append('Gustavo')
teste.append('40')
galera = list()
galera.append(teste[:]) # LIGAÇÃO ENTRE AS DUAS ESTRUTURAS, SE MUDAR UMA TEM QUE MUDAR OUTRA. RESOLVE-SE FAZENDO UMA CÓPIA
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
# [:] PARA FAZER UMA CÓPIA

#_____________________________________________________________________________________________________________________

galera = [['João',19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0]) # GALERA 0 = 'JOÃO' 19 ANOS MAS [0][0] SÓ EXIBE O 'JOÃO'
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#_____________________________________________________________________________________________________________________

galera = list()
dados = list()
totmaior = totmenor = 0
for c in range (0,3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:]) #PRECISA FAZER CÓPIA DE 'DADOS' OU O COMANDO CLEAR ABAIXO APAGARÁ AS IFORMAÇÕES INSERIDAS
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1

print(f'Temos {totmaior} pessoa(s) maior(es) de idade e {totmenor} pessoa(s) menor(es) de idade.')



