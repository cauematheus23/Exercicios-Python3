"""   Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.   """

c = 0
ptermo = int(input("Digite o primeiro termo de uma P.A: "))
razao = int(input("Digite a razão dessa P.A: "))
a= ptermo
print('A P.A de Primeiro termo {} e Razão {} é '.format(ptermo,razao),end ='')
print()
b =10
while c < b:
    print('\033[34m{}\033[m'.format(a),end='')
    print(' \033[31m-> \033[m' if c < 9 else '',end='')
    a += razao
    c += 1