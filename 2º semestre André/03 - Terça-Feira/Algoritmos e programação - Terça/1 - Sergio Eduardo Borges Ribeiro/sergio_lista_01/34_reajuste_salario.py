# 34. Receba o salário de um funcionário e calcule o reajuste: aumento de 15%
#     para salários até R$ 1.500,00 e 10% para salários superiores.

salario = float(input("Digite o salário do funcionário: "))

if salario <= 1500.00:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10

print(f"Novo salário: R$ {novo_salario:.2f}")
