"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""
time = list()
jogador = dict()
partidas = list()
while True:
    print('-'*40)
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou ? "))
    partidas.clear()
    for c in range (0,tot):
        partidas.append(int(input(f"    Quantos gols na partida {c+1} ? ")))
    jogador['gols'] = partidas[:]
    jogador ['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        sn = str(input("Quer continuar? [S/N] ")).upper()
        if sn in 'SN': 
            break
        print('ERRO! RESPONDA APENAS COM S OU N.')
    if sn in 'Nn':
        break
print("="*40)
print('cod    ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*40)
for k ,v in enumerate(time):
    print(f'{k}    ', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()
while True: 
    print('-'*45)
    busca = int(input("Mostrar dados de qual jogador? "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! O JOGADOR {busca} não existe')
    else:
        print(f"--- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}")
        for c in range(0,len(time[busca]['gols'])):
            print(f"    No jogo {c+1} fez {time[busca]['gols'][c]} gols.")
            
print("PROGRAMA ENCERRADO, OBRIGADO POR USAR.")