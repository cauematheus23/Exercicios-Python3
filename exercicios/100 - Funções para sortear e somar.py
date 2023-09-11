"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""
from random import randint
from time import sleep
valores = list()
pares = list()
def sorteia():
    print('--'*50)
    print("Sorteando 5 valores... ",end = ' ')
    for c in range(0,5):
        a = randint(1,50)
        print(a,end=' ',flush=True)
        sleep(0.5)
        valores.append(a)
    print()

def somapar():
    p = 0
    for i in valores:
        if i % 2 == 0:
            p += i
            pares.append(i)
    print(f"A soma dos valores pares de {valores} é = {p}")
sorteia()
somapar()
