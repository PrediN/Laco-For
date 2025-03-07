# 11. Faça um programa que peça para N pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma
# varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.


# Declaração de variaveis

idade = 0
mediaIdade = 0
numeroPessoas = int(input("Digite o número de pessoas: "))

# Apresentação de resultados

for i in range(numeroPessoas):
    idade = int(input("Digite a idade: "))
    mediaIdade += idade

mediaIdade /= numeroPessoas

if mediaIdade >= 0 and mediaIdade <= 25:
    print("A turma é jovem")

elif mediaIdade >= 26 and mediaIdade <= 60:
    print("A turma é adulta")

else:
    print("A turma é idosa")