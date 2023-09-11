"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """
l = []
mai = 0
men = 0
for i in range (0,5):
    l.append(int(input("Digite um valor: ")))
    if i == 0:
        mai = men = l[i]
    else:
        if l[i] > mai:
            mai = l[i]
        if l[i] < men:
            men = l[i]
print('='*30)
print(f"Você digitou os valores {l}")
print(f"O maior valor digitado foi {mai} nas posições ",end='')
for c, v in enumerate(l):
    if v == mai:
        print(f"{c}...",end='')
print()
print(f"O menor valor digitado foi {men} nas posições ",end='')
for c, v in enumerate(l):
    if v ==men:
        print(f"{c}...",end='')
print()
