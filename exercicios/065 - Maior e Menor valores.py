"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

cont = 0
b = 0
a = 's'.upper()
lista = []
c = 0
while a == 'S' or a == 'SIM':
    c = int(input("Digite um Valor: "))
    cont += 1
    b += c
    media = b / cont
    lista.append(c)
    a = str(input("DIGITE [SIM] PARA DIGITAR OUTRO VALOR E [NÃO] SE DESEJA PARAR: ")).upper()
print('Você digitou {} numeros cuja soma é igual a {} e a media entre eles é {} , sendo o maior valor digitado {} e o menor {} '.format(cont,b,media,max(lista),min(lista)))