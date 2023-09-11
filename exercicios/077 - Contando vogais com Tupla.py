"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
print('-'*60)
print(f"{'VOGAIS EM PYTHON':^60}")
print('-'*60)

for c in palavras:
    print(f"Na palavra \033[33m{c:<10}\033[m temos as seguintes vogais: ",end='')
    for i in c:
        if i.lower() in 'aeiou':
            print(f"\033[34m{i}\033[m",end='')
    print('')
    

