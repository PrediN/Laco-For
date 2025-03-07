# 13. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

# Declaração de variáveis

pares = 0
impares = 0
numeros = 0

# Apresentação de resultados

for i in range(10):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números impares: {impares}")