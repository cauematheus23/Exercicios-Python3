"""   Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.   """
from time import sleep
num = int(input("Digite um número: "))
print("Para um número ser primo tem que ser divisivel apenas por 1 e por ele mesmo.")
print("Verificando...")
sleep(3)
cont = 0
for c in range(1,num + 1):
    if num % c == 0:   
        print("\033[34m",end='')
        cont += 1
    else:
        print("\033[m",end='')
    print('{}'.format(c),end=' ')
print('\033[m')
if cont <= 2:
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")
#FEITO COM LISTA
'''num = int(input("Digite um valor: "))
cont = 0
lista = []
for c in range (1,num +1):
    if num % c == 0:
        lista.append(c)
        cont += 1
if cont > 2:
    print(f"O número {num} não é um numero primo pois ele é divisivel por {lista}")
else:"""
    print(f"O número {num}  é um numero primo pois ele é divisivel apenas por {lista}")'''




