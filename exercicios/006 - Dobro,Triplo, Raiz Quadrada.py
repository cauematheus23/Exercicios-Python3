""" Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada   """
import math
n = int(input("Digite um número: "))
d = n * 2
t = n * 3
rq = math.sqrt(n)
print(f"Analisando o número {n}, seu dobro é {d}, seu triplo é {t} e sua raiz quadrada é {rq}")
