"""   Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).   """
soma = cont = 0
while True:
    n = int(input("Digite um valor (999 para finalizar.)\n\033[35m--> \033[m"))
    if n == 999:
        break
    soma +=n
    cont += 1
print(f"Você digitou \033[34m{cont}\033[m numeros e a soma deles é \033[34m{soma}\033[m")
