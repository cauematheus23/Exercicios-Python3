""" Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a porção inteira 6.          """

import math 
num = float(input("Digite um numero: "))
pi = math.trunc(num)
print(f"O valor digitando foi {num} e sua porção inteira é {pi}")