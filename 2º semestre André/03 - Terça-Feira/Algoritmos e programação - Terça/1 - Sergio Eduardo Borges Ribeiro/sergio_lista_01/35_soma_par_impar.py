# 35. Leia dois números inteiros e informe se a soma deles é par ou ímpar.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

if soma % 2 == 0:
    print(f"A soma ({soma}) é par")
else:
    print(f"A soma ({soma}) é ímpar")
