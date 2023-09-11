"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import sample
from time import sleep
jogos = []
print("-"*40)
print("      JOGOS MEGA SENA      ")
print("-"*40)
q = int(input("Quantos jogos quer que eu sorteie? "))
print("-="*3,end='')
print(f" SORTEANDO {q} JOGOS ",end='')
print("-="*3)
for c in range (0, q):
    jogos.append(sample(range(0,61),6))
    jogos[0].sort()
    sleep(1)
    print(f"Jogo {c+1}: {jogos}")
    jogos.clear()
print('='*40,end='')
print(" BOA SORTE ",end='')
print('='*40)