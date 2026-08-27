# 43. Peça o valor de um produto e a forma de pagamento (1: À vista dinheiro/PIX
#     - 10% desconto, 2: Cartão à vista - valor normal, 3: Parcelado - 5% de
#     juros). Exiba o valor final.

valor = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Forma de pagamento (1-Dinheiro/PIX, 2-Cartão à vista, 3-Parcelado): "))

if forma_pagamento == 1:
    valor_final = valor * 0.90
    print(f"Pagamento à vista (Dinheiro/PIX) - Valor final: R$ {valor_final:.2f}")
elif forma_pagamento == 2:
    valor_final = valor
    print(f"Pagamento no Cartão à vista - Valor final: R$ {valor_final:.2f}")
elif forma_pagamento == 3:
    valor_final = valor * 1.05
    print(f"Pagamento Parcelado - Valor final: R$ {valor_final:.2f}")
else:
    print("Forma de pagamento inválida")
