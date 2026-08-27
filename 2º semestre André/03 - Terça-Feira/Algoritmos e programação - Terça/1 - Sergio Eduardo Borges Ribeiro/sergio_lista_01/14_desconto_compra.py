# 14. Solicite o valor total de uma compra. Se for maior que R$ 100, aplique um
#     desconto fictício e informe "Desconto aplicado", senão exiba "Valor integral".

DESCONTO = 0.10  # 10% de desconto fictício
valor = float(input("Digite o valor total da compra: "))

if valor > 100:
    valor_final = valor * (1 - DESCONTO)
    print(f"Desconto aplicado - Valor final: R$ {valor_final:.2f}")
else:
    print(f"Valor integral: R$ {valor:.2f}")
