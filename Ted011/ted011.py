# Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos.
# Depois: Imprima o resultado da soma de todos os valores da matriz no terminal;
# E, crie uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

from random import randint
from time import sleep

matriz1 = []
for linha in range(10):
    linha = []
for coluna in range(10):
    linha.append(randint(0, 100))
    matriz1.append(linha)
print('-='*20)        
print('Criando Matriz..')
print('-='*20)
sleep(1)
print(matriz1)

soma = 0
for linha in range(len(matriz1)):
        for coluna in range(len(matriz1)):
            soma += matriz1[linha][coluna]
print('Temos aqui a soma total da matriz A: ', soma)

# segunda parte #

matriz2 = []

for linha in range(0, len(matriz1)):

    lista_aux = []

    for c in range(0, len(matriz1[1])):
        resultado_multiplicação = matriz1[1][c] * 3
        lista_aux.append(resultado_multiplicação)

    matriz2.append(lista_aux)

print('Resultado da matriz B é ',matriz2)
