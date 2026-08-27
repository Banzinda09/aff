# 12. Leia a altura e o peso de uma pessoa. Se a altura for menor que 1.50,
#     exiba "Abaixo da altura mínima".

altura = float(input("Digite a altura (m): "))
peso = float(input("Digite o peso (kg): "))

if altura < 1.50:
    print("Abaixo da altura mínima")
else:
    print("Altura dentro do esperado")
