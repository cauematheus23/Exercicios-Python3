"""   Crie um programa que faça o computador jogar Jokenpô com você.   """

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''SUAS ESCOLHAS
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
eu = int(input('Qual sua jogada? '))
print('-=' * 11)
if eu != 0 and eu != 1 and eu != 2:
    print('Valor invalido tente novamente')
else:
    print(f'A maquina escolheu {itens[pc]}')
    print(f'Você escolheu {itens[eu]}')
    print('-=' * 11)
    if eu == 0 and pc == 0:
        print('EMPATE')
    if eu == 1 and pc == 1:
        print('EMPATE')
    if eu == 2 and pc == 2:
        print('EMPATE')
    elif eu == 0 and pc == 1:
        print('DERROTA')
    elif eu == 0 and pc == 2:
        print('VITÓRIA')
    elif eu == 1 and pc == 0:
        print('VITÓRIA')
    elif eu == 1 and pc == 2:
        print('DERROTA')
    elif eu == 2 and pc == 0:
        print('DERROTA')
    elif eu == 2 and pc == 1:
        print('VITÓRIA')
