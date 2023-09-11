"""   Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).   """
cont = 0
a = 0
b = 0
while a != 999:
    a = int(input("Digite um valor (999 para finalizar.)\n\033[35m--> \033[m"))
    cont += 1
    b += a
print('Você digitou {} numeros e a soma entre eles é {}'.format(cont -1 ,b -999))