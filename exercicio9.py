# 9. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

# Declaração de variaveis
num = int(input("Digite o número desejado: "))

# Apresentação de resultados

if num < 0:
    print("O número digitado é negativo. Por favor, insira um número positivo.")

elif num == 0:
    print("O número 0 não é primo.")

elif num == 1:
    print("O número 1 não é primo.")

elif num == 2:
    print("O número 2 é primo.")

else:
    for i in range(2, num):
        if num % i == 0:
            print(f"O número {num} não é primo.")
            break
    else:
        print(f"O número {num} é primo.")