"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""
expr = str(input("DIGITE A EXPRESSÃO: "))
pilha=[]
for c in expr: #navega pela expressão
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressãoe está correta")
else:
    print("Sua expressãoe está errada")