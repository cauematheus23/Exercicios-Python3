"""   Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.   """

soma = 0 # Feito com 
cont = 0
for c in range (1,7):
    num = int(input(f"Digite o {c}° valor: "))
    if num % 2 == 0:
        soma += num
        cont +=1
print(f"Você digitou {cont} numeros pares e a soma deles é {soma}")

""" FEITO COM LISTA """
soma = 0 
lista = [] #lista pra receber os valores pares
for c in range(0,6): #rodar 6 vezes o programa
    a = int(input("Digite um valor: ")) #receber o valor digitado pelo usuario
    if a % 2 == 0 : #verificar se é par
        soma += a #mesma coisa que soma = soma + a
        lista.append(a)#função pra inserir valores em uma lista
print(f"a soma de {lista} é {soma}") 