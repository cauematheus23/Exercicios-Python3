"""   Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.    """
from time import sleep
while True:
    print ('-'*30)
    n = int(input("Quer ver a tabuada de qual valor? "))
    print('-'*30)
    if n < 0 :
        break
    for c in range (1,11):
        print(f"\033[34m{n}\033[m x \033[34m{c}\033[m = \033[34m{n * c}\033[m")
        sleep(0.5)
    
print("PROGRAMA ENCERRADO.")