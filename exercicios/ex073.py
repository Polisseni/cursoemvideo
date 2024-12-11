times = ('Corinthians','Palmeiras','Santos','Grêmio',
         'Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atlético','Botafogo','Atlético-PR','Bahia',
         'São Paulo','Fluminense','Sport','Vitória',
         'Coritiba','Avaí','Ponte-Preta','Atlético-GO')
print('-'*20)
print(f'Os times do brasileirão de 2017 são: {times}')
print('-'*20)
print(f'Os primeiros são {times[0:5]}')
print('-'*20)
print(f'Os últimos times são {times[-4:]}')
print('-'*20)
print(f'Os times em ordem alfabética são {sorted(times)}')
print('-'*20)
print(f'O Chapecoense está na posição {times.index("Chapecoense")+1}ªposição')