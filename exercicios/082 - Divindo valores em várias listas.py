"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""
c=int(input("Gostaria de digitar quantos valores?:"))
l = []
limp = []
lpar = []
for i in range (0,c):
    a = int(input("Digite um valor: "))
    l.append(a)
    if a % 2 == 0:
        lpar.append(a)
    else:
        limp.append(a)
print('='*60)
print(f"Lista Completa: {l}\nLista Impar: {limp}\nLista Par: {lpar}")