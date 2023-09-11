"""   Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.   """

extenso = 'zero', 'um', 'dois', 'três', 'quatro', \
          'cinco', 'seis', 'sete', 'oito', 'nove', \
          'dez', 'onze', 'doze', 'treze', 'quatorze', \
          'quinze', 'dezesseis', 'dezesseta', 'dezoito', \
          'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n > 20:
        print('Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {extenso[n]}.')
        continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break

