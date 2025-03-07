# 6. Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.

for i in range(10):
    for s in range(10):
        print(f"{i+1}×{s+1}=", (i+1)*(s+1))
    print()