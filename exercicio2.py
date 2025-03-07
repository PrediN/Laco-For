# 2. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

# Declaração de variaveis
num1 = int(input("Insira o número inicial: "))
num2 = int(input("Insira o número final: "))

if num1 < num2:
    for i in range(num1, num2+1):
        print(i, end=" ")

else:
    for i in range(num2, num1+1):
        print(i, end=" ")