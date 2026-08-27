# 5. Leia uma temperatura em Celsius e exiba "Congelante" se for menor ou igual a 0,
#    e "Normal" caso contrário.

temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura <= 0:
    print("Congelante")
else:
    print("Normal")
