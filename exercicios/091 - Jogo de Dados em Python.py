"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
dado = dict()
for c in range (1,5):
    dado[f'Jogador {c}'] = randint(1,6)
    print(f' Jogador {c} tirou {dado[f"Jogador {c}"]}')
    sleep(1)
print('RANKING')
for key, value in enumerate(sorted(dado, key=dado.get, reverse=True)):
    print(f'    {key + 1}° lugar: {value} com {dado[value]}')
    sleep(0.5)