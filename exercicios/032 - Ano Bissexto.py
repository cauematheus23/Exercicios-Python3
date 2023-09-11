"""  Faça um programa que leia um ano qualquer e mostre se ele é Bissexto   """
from datetime import datetime
ano = int(input("Qual ano deseja analisar?(O para o ano atual) "))
if ano == 0:
    ano = datetime.now().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissexto")
else:
    print(f"O ano {ano} não é Bissexto")