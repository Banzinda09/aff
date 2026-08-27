# 42. Escreva um programa para aprovar um empréstimo bancário: peça o valor da
#     casa, o salário e em quantos anos vai pagar. A prestação mensal não pode
#     exceder 30% do salário.

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
anos = int(input("Digite em quantos anos vai pagar: "))

meses = anos * 12
prestacao = valor_casa / meses
limite_prestacao = salario * 0.30

print(f"Prestação mensal: R$ {prestacao:.2f}")

if prestacao <= limite_prestacao:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado: a prestação excede 30% do salário")
