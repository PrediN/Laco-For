"""
16. Faça um programa que receba a idade de 15 pessoas e que calcule e
mostre:
a) A quantidade de pessoas em cada faixa etária;
b) A percentagem de pessoas na primeira e na última faixa etária, com
relação ao total de pessoas:
 Até 15 anos
 De 16 a 30 anos
 De 31 a 45 anos
 De 46 a 60 anos
 Acima de 61 anos
"""

# Declaração de variáveis
idade = 0
crianca = 0
jovem = 0
adulto = 0
idoso = 0
melhorIdade = 0
totalPessoas = 15

# Apresentação de resultados
for i in range(15):
    idade = int(input("Digite a idade da pessoa: "))
    if idade <= 15:
        crianca += 1
    elif idade <= 30:
        jovem += 1
    elif idade <= 45:
        adulto += 1
    elif idade <= 60:
        idoso += 1
    else:
        melhorIdade += 1

print()
print("Quantidade de pessoas em cada faixa etária:")
print(f"Quantidade de crianças: {crianca}")
print(f"Quantidade de jovens: {jovem}")
print(f"Quantidade de adultos: {adulto}")
print(f"Quantidade de idosos: {idoso}")
print(f"Quantidade de pessoas da melhor idade: {melhorIdade}")
print()

print("Percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:")
print(f"Percentual de crianças: {crianca / totalPessoas * 100:.2f}%")
print(f"Percentual de pessoas da melhor idade: {melhorIdade / totalPessoas * 100:.2f}%")