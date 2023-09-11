"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
import datetime
y = datetime.date.today().year
def voto(ano=1):
    a = ("VOTO NEGADO")
    b = ("VOTO OBRIGATORIO")
    c = ("VOTO OPCIONAL")
    if i < 18:
        return a
    elif i > 18 and i < 65:
        return b
    else:
        return c
    
print("-"*50)
ano = int(input("Qual seu ano de nascimento: "))
i = y - ano
print(f'Com {i} anos: {voto(ano)}')
