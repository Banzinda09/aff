# 19. Peça o salário de um funcionário. Se for maior que R$ 3.000,00, informe que
#     ele paga Imposto de Renda; caso contrário, informe que está isento.

salario = float(input("Digite o salário do funcionário: "))

if salario > 3000.00:
    print("Paga Imposto de Renda")
else:
    print("Isento de Imposto de Renda")
