# 30. Valide uma divisão: receba o numerador e o denominador. Se o denominador
#     for 0, exiba "Erro: divisão por zero"; caso contrário, exiba o resultado.

numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))

if denominador == 0:
    print("Erro: divisão por zero")
else:
    print(f"Resultado: {numerador / denominador}")
