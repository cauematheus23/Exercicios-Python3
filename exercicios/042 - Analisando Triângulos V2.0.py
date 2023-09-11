"""   Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes   """
r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os valores inseridos são capazes de formar um triângulo')
    sim = str(input('\033[1;35mQuer saber qual o tipo do triângulo formado?\033[m ')).upper()
    if sim == 'SIM':
        if r1 == r2 and r1 == r3:
            print(f'Com as retas \033[34m{r1, r2, r3,}\033[m forma-se um \033[34mTriângulo Equilátero\033[m cujos 3 lados são iguais')
        elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:
            print(f'Com as retas \033[34m{r1, r2, r3,}\033[m forma-se um \033[34mTriângulo Isósceles\033[m cujo apenas um lado é diferente')
        else:
            print(f'Com as retas \033[34m{r1, r2, r3,}\033[m forma-se um \033[34mTriângulo Escaleno\033[m cujo os 3 lados são diferentes')
    else:
        print('Okay tenha um bom dia')
else:
    print('\033[1;31mNão é capaz de formar um triângulo\033[m')