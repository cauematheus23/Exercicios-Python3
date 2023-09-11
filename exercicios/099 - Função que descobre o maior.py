"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep
def maior(*num):
    ma =  0
    cont = 0
    print("--"*40)
    print(f"Analisando os valores passados...")
    for v in num:
        print(v,end='  ',flush=True)
        sleep(0.5)
        cont +=1
        if v > ma :
            ma = v
        
    print(f"Foram informados {cont} valores ao todo.")
    print(f"Sendo o maior valor informado {ma}")
    print("--"*40)

maior(10,2,3,4,7,32,1)
maior(0,1,2,3,4,5,6,7,8,9)
maior(100,12,14,16,92,1023)