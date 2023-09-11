"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""
gols = list()
jogador = {'nome': str(input("Nome do Jogador: "))}
a = int(input(f"Quantas partidas {jogador['nome']} jogou ? "))
for c in range (0,a):
    gols.append(int(input(f"Quantos gols na partida {c+1} ?  ")))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
for k, v in jogador.items(): 
    print(f"{k} tem valor {v}")
print('=-'*30)
print(f"O jogador {jogador['nome']} jogou {a} partidas. ")
for i in range(0,a):
    print(f"Na partida {i+1}, fez {gols[i]} gols.")
print(f"Foi um total de {jogador['total']} gols")