"""   Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120   """

n = int(input("digite o numero para saber seu fatorial: "))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print("\033[34m{}\033[m".format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c # F = f * c
    c -= 1
print('{}'.format(f))

#UTILIZANDO FOR
n = int(input("digite o numero para saber seu fatorial: "))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for i in range (f,n+1):
    print("{}".format(c), end='')
    print(' x ' if c>1  else ' = ',end='')
    f *= c # F = f * c
    c -= 1

print('{}'.format(f))
