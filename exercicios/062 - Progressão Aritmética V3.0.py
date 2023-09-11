"""   Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.   """

c = 0
ptermo = int(input("Digite o primeiro termo de uma P.A: "))
razao = int(input("Digite a razão dessa P.A: "))
a= ptermo
print('A P.A de Primeiro termo = {} e Razão  {} é '.format(ptermo,razao),end ='')
b =11
while c <= b:
    if c == 10:
        b = int(input("\nGostaria de ver quantos termos mais? "))+9
    print('\033[34m{}\033[m'.format(a),end='')
    print(' \033[31m-> \033[m' if c < b else '',end='')
    a += razao
    c += 1