# 25. Peça um número e verifique se ele é divisível por 3 e por 5 simultaneamente.

numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e por 5")
else:
    print("O número NÃO é divisível por 3 e por 5 simultaneamente")
