print('TABELA DO BRASILEIRÃO 22/05/2018')
print('-=-'*20)
times = ('Atlético Mineiro', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 'América - MG', 'São Paulo', 'Grêmio',
         'Vasco da Gama', 'Internacional', 'Botafogo', 'Sport Recife', 'Cruzeiro', 'Vitória', 'Santos', 'Chapecoense',
         'Atlético - PR', 'Bahia', 'Ceará', 'Paraná')
chapecoense = times.index('Chapecoense')+1
print(f'Lista de times do Brasileirão:{times}')
print('-=-'*20)
print(f'Os 5 primeiros colocados do Brasileirão são {times[:5]}')
print('-=-'*20)
print(f'Os últimos 4 colocados do Brasileirão são {times[-4:]}')
print('-=-'*20)
print('A lista em ordem alfabética é:')
print(sorted(times))
print('-=-'*20)
print(f'A Chapecoense está na {chapecoense}ª posição')
#print(times.index('Chapecoense')+1)

