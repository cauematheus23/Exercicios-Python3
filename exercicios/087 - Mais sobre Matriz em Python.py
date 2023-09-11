"""Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[],[],[]]
a = 0
x = 0
ma = 0
for c in range (0,3):
    for i in range(0,3):
        b=(int(input(f"Digite um valor para [{c}][{i}]: ")))
        matriz[c].append(b)
        if b % 2==0:
            a += b
        if i == 2:
            x += b
print("="*40)
for c in range (0,3):
    for i in range(0,3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
print("=" *40)
for c in matriz[1]: 
    if c > ma:
        ma = c
print(f"A soma de todos os valores pares digitados é: {a}")
print(f"A soma dos valores da Terceira coluna é: {x}")
print(f"O maior valor da segunda linha é: {ma}")