"""   Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.   """


"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense."""
times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo',
'AthleticoParanaense','AtléticoMineiro','Fortaleza','São Paulo','AméricaFcSaf','Botafogo',
'Santos','Goiás','RedBullBragantino','Coritiba','Cuiabá Saf','Ceará','AtléticoGO','Avaí','Juventude')
print(f"OS 5 PRIMEIROS TIMES SÃO {times[0:5]}")
print('-'*30)
print(f"OS 4 ULTIMOS TIMES SÃO {times[-4:]}")
print('-'*30)
print(f"OS TIMES EM ORDEM ALFABETICA SÃO {sorted(times)}")
print('-'*30)
print(f"O Corinthians esta na {times.index('Corinthians')+1}° posição.")