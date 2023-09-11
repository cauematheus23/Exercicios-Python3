"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
l = []
lista = []
ma = me = 0
while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))
    if len(l) == 0:
        ma = me = lista[1]
    else:
        if lista[1] > ma:
            ma = lista[1]
        if lista[1] < me:
            me = lista[1]
    l.append(lista[:])
    lista.clear()
    c = str(input("Deseja cadastrar outra pessoa? [S/N]: "))
    if c in "Nn":
        break
print('='*30)
print(f"Ao todo foi cadastrado {len(l)} pessoas ")
print(f'O maior peso foi {ma:.2f} ',end='')
for p in l:
    if p[1] == ma:
        print(p[0],end='')
print()
print(f"O menor peso foi {me:.2f} ",end='')
for p in l:
    if p[1] == me:
        print(p[0] ,end='')
print()