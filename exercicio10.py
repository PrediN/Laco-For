# 10. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
# valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

# Declaração de variaveis
faturamento = 0
vendasLojaA = 0
vendasLojaB = 54000

# Apresentação de resultados

for i in range(5):
    vendasLojaA = float(input("Digite o valor das vendas da loja A: "))
    faturamento += vendasLojaA

if faturamento > vendasLojaB:
    print(f"O faturamento da loja A foi superior ao da loja B em R${faturamento - vendasLojaB}.")

else:
    print(f"O faturamento da loja A não foi superior ao da loja B.")