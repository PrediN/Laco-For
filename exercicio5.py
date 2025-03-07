# 5. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

# Declaração de variaveis
numMultiplo = int(input("Digite o número que desejada: "))

# Apresentação de resultados

for i in range(10):
    print(f"{i+1} × {numMultiplo} =", (i+1)*numMultiplo)