"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
list= []
i = 0
while True:
    list.append(int(input("Digite um valor: ")))
    i +=1
    a = str(input("Deseja continuar? [S/N]"))
    if a in 'Nn':
        break
list.sort(reverse=True)
print('+'*60)
print(f"foram digitados {i} valores")
print(f"os valores em ordem decrescente são {list}")
if 5 in list:
    print("O valor 5 faz parte da lista lista ")
else:
    print("O valor 5 não faz parte da lista")
