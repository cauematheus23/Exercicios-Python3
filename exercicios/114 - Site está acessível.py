"""Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""
from urllib import request,error
def tPudim():
    try:
        site = request.urlopen("http://www.pudim.com.br")
    except error.URLError:
        print("\033[31mNão foi possivel acessar o site pudim.com.br no momento\033[m")
    else:
        print("\033[32mConsegui acessar o site pudim.com.br com sucesso!\033[m")
    

tPudim()