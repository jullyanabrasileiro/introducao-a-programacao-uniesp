#Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

import random

numeros = []
VET = []

for x in range(1, 51):
    VET.append(random.randint(1, 9))

for y in VET:
    if y not in numeros:
        indices = [indices for indices, valor in enumerate(VET) if valor == y]
        print("O número: ", y , "se repete nas posições: ", indices)
        numeros.append(y)

 