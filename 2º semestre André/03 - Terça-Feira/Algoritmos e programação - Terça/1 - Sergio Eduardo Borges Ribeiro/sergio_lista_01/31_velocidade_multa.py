# 31. Receba a velocidade de um carro. Se for maior que 80 km/h, exiba "Multado!".
#     Caso contrário, exiba "Velocidade permitida".

velocidade = float(input("Digite a velocidade do carro (km/h): "))

if velocidade > 80:
    print("Multado!")
else:
    print("Velocidade permitida")
