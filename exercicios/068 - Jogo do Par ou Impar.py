"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """
from random import randint
cont = 0
while True:
    pi = int(input("Digite \n\033[34m1- [ PAR ] \n2-[ IMPAR ]\n--> \033[m "))
    while pi != 1 and pi != 2:
        print("Por Favor digite um valor valido: ")
        pi = int(input("Digite \n1-[PAR] \n2-[IMPAR]\n: "))
    pc = randint(1,10)
    eu = int(input("Escolha um numero para jogar: "))
    par = (pc + eu) % 2

    if par == 0 and pi == 1:
        print(f"Maquina = {pc} \nJogador = {eu} \nSoma = {pc + eu}\nPARABENS VOCE VENCEU O RESULTADO FOI PAR")
    if par == 1 and pi == 2:
        print(f"Maquina = {pc} \nJogador = {eu} \nSoma = {pc + eu}\nPARABENS VOCE VENCEU O RESULTADO FOI IMPAR")
    if par == 0 and pi == 2:
        print(f"Maquina = {pc} \nJogador = {eu} \nSoma = {pc + eu}\nVOCE PERDEU POIS O RESULTADO FOI PAR")
        break
    if par == 1 and pi == 1:
        print(f"Maquina = {pc} \nJogador = {eu} \nSoma = {pc + eu}\nVOCE PERDEU POIS O RESULTADO FOI IMPAR")
        break
    cont +=1
print(f"Programa encerrado, parabens por vencer {cont} vezes")