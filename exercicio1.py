# 1. Faça um programa que leia 5 números e informe o maior número.

# Declaração de variaveis

maior = 0
numero = 0

# Apresentação de resultados

for i in range(5):
    numero = int(input("Digite o número desejado: "))

    if numero > maior:
        maior = numero

    print(f"Número digitado: {numero}. Maior número: {maior}")