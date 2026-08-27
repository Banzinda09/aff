# 37. Simule um caixa eletrônico: solicite o valor de um saque e informe se o
#     valor é válido (deve ser um valor positivo e múltiplo de 10).

valor = float(input("Digite o valor do saque: "))

if valor > 0 and valor % 10 == 0:
    print("Valor válido para saque")
else:
    print("Valor inválido. O saque deve ser positivo e múltiplo de 10")
