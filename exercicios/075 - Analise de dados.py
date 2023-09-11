"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

tupla = (int(input("Digite um valor: ")),int(input("Digite um valor: ")),int(input("Digite um valor: ")),int(input("Digite um valor: ")))#podia ser feito com tupla = tuple(int(input("Digite um valor: ")) for c in range (1,5))

        
print(f"O numero 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O primeiro numero 3 aparece na {tupla.index(3)+1}° posição")
else:  
    print(f"Não digitado o valor 3 em nenhuma posição.")
print('Os valores pares digitados foram ',end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')