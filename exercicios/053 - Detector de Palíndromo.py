"""   Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.   """

frase= str(input('Digite uma frase; ')).strip().upper() #Jogou tudo para letra maiuscula
palavras = frase.split() #separou os espaços em string
junto = ''.join(palavras) #juntou tudo numa só string
inverso = '' 
#inverso = junto[::-1] # outra forma de se fazer sem precisar do for
for letra in range(len(junto)-1,-1,-1): #inverteu a string indo da ultima letra até a primeira
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('Não temos um Palíndromo')