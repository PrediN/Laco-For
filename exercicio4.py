# 4. Faça um programa que leia 5 números e informe a soma e a média dos números.

# Declaração de variaveis

soma = 0
numero = 0

# Apresentação de resultados

for i in range(5):
    soma += int(input(F"Digite a {i+1}ª nota: "))


print(f"A Soma das notas são: {soma}")
print(f"A média dos números é {soma/5}")
