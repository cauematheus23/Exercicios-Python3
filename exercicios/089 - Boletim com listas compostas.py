"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""
from time import sleep  
boletim = list()
cont = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    boletim.append([nome,[n1,n2],media])
    cont += 1
    c = str(input("Deseja continuar? [S/N]: "))
    if c in 'Nn':
        break
print("="*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-'*30)
for c in range (0,cont):
    print(f'{c:<4}{boletim[c][0]:<10}{boletim[c][2]:<8}')
while True:
    print('-'*30)
    a = int(input("Digite o numero que deseja ver as notas (999 PARA O PROGRAMA): "))
    if a == 999:
        print('FINALIZANDO...')
        break
    if a <= len(boletim)-1:
        print(f'Notas de {boletim[a][0]} são {boletim[a][1]}')       