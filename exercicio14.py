# 14. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

# Declaração de variáveis

notas = 0

# Apresentação de resultados

for i in range(5):
    notas = float(input("Digite uma nota entre 0 e 10: "))
    if notas < 0 or notas > 10:
        print("Nota inválida, digite uma nota entre 0 e 10")
    else:
        print("Nota válida")
        break