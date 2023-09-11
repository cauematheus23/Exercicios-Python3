"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores."""
from time import sleep
def sistemadeajuda():
    while True:
        print('\033[1;97mSistema de Ajuda do Python\033[m')
        funbib = str(input('\033[1;34mFunção ou Biblioteca >\033[m ')).strip().lower()
        if funbib == 'fim':
            print('Programa encerrado. Volte sempre!')
            return
        print(f'\033[1;33mAcessando o manual do "{funbib}"\033[m')
        sleep(1.5)
        help(f'{funbib}')


sistemadeajuda()


