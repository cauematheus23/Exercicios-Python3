"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

a = int(input("digite um numero para ver sua tabuada: "))
for c in range(0,11): #contar de um até 10
    print(f"{a} x {c} = {a*c}")