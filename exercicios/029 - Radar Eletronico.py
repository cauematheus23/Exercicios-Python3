""""   Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.   """
print("\033[33m-=\033[m"*30)
print("\033[35mRADAR ELETRONICO\033[m")
print("\033[33m-=\033[m"*30)
v = int(input("Qual a velocidade do veiculo: "))
if v <=80 :
    print("\033[32mMuito bom, continue dirigindo dentro dos limites.\033[m")
else:
    print(f"\033[31mVocê foi multado no valor de R${(v-80)*7},00 por passar {v-80}Km/h acima do limite de 80Km/h.\033[m")
