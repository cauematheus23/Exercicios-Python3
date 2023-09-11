"""   Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.   """

from datetime import date
nasc = int(input('Em que ano você nasceu: '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    a = 18 - idade
    print(f'Quem nasceu em {nasc} tem {idade} anos.')
    print(f'Ainda faltam {a} anos para seu alistamento.')
    print(f'Seu alistamento será em {ano + a}.')
elif idade > 18:
    a = idade - 18
    print(f'Quem nasceu em {nasc} tem {idade} anos.')
    print(f'Era pra você ter se alistado à {a} anos atrás')
    print(f'Seu alistamento foi em {ano - a}.')
else:
    print('Parabéns chegou seu ano de alistamento, vá se alistar')
