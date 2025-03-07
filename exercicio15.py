"""
15. Uma loja tem tem uma política de descontos de acordo com o valor da
compra do cliente. Os descontos começam acima dos R$500. A cada 100
reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
25%.
Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
Faça um programa que exiba essa tabela de descontos no seguinte formato:
Valordacompra – porcentagem de desconto – valor final
"""

# Declaração de variáveis

valorCompra = 0
desconto = 0
valorFinal = 0

# Apresentação de resultados

valorCompra = float(input("Digite o valor da compra: "))

if valorCompra > 500:
    desconto = (valorCompra - 500) // 100
    if desconto > 25:
        desconto = 25
    valorFinal = valorCompra - (valorCompra * (desconto / 100))
    print(f"Valor da compra: R${valorCompra:.2f} - Desconto: {desconto}% - Valor final: R${valorFinal:.2f}")

else:
    print(f"Valor da compra: R${valorCompra:.2f} - Desconto: 0% - Valor final: R${valorCompra:.2f}")
    