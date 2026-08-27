# 29. Crie uma calculadora simples: leia dois números e um operador (+, -, *, /)
#     e exiba o resultado.

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = None
        print("Erro: divisão por zero")
else:
    resultado = None
    print("Operador inválido")

if resultado is not None:
    print(f"Resultado: {resultado}")
