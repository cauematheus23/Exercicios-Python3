"""   Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu.   """
from random import randint
from time import sleep
pc = randint(0,5)
print("\033[33m-=\033[m"*30)
print("\033[34mVou Pensar em um Número de 0 a 5. Tente Advinhar\033[m")
print("\033[33m-=\033[m"*30)
u = int(input("Em que número eu pensei? "))
print("\033[35mPROCESSANDO...\033[m")
sleep(3)
if u >= 0 and u <=5:
    if u == pc: 
        print("\033[32mPARABENS VOCÊ ACERTOU\033[m")
    else:
        print(f"\033[31mERROOOOUUUU!! Eu pensei no número {pc} \033[m")
else:
    print("Por favor digite um valor entre 0 e 5.")