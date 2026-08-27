# 41. Receba o valor do peso e da altura, calcule o IMC (IMC = peso / altura^2)
#     e informe a faixa: Abaixo do peso (< 18.5), Peso normal (18.5-24.9),
#     Sobrepeso (25-29.9) ou Obesidade (>= 30).

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    faixa = "Abaixo do peso"
elif imc < 25:
    faixa = "Peso normal"
elif imc < 30:
    faixa = "Sobrepeso"
else:
    faixa = "Obesidade"

print(f"IMC: {imc:.2f} - {faixa}")
