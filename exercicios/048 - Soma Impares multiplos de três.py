"""   Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.   """

soma=0
cont = 0
for c in range (0,501): # Repetir 500x
    if c % 2 == 1: #verificando se é impar
       if c % 3 == 0 : #verificando se é multiplo de 3
            soma += c # mesma coisa que soma= soma+c
            cont += 1
            print(c,end=' ')
print()
print(f"a Soma de todos os {cont} valores impares e multiplos de 3 entre 1 e 500 é {soma}")