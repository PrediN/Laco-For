# 12. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

# Declaração de variaveis
candidato1 = 0
candidato2 = 0
candidato3 = 0
votos = 0
numeroEleitores = int(input("Digite o número total de eleitores: "))

# Apresentação de resultados

for i in range(numeroEleitores):
    print()
    print("Candidatos:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print()

    votos = int(input("Digite o número do candidato: "))

    if votos == 1:
        candidato1 += 1

    elif votos == 2:
        candidato2 += 1

    elif votos == 3:
        candidato3 += 1

print()
print("Candidato 1: ", candidato1)
print("Candidato 2: ", candidato2)
print("Candidato 3: ", candidato3)
