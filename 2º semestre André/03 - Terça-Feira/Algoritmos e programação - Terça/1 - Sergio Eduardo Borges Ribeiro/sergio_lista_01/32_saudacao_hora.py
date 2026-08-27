# 32. Escreva um programa que receba a hora atual (0 a 23) e exiba "Bom dia"
#     (5-11), "Boa tarde" (12-17) ou "Boa noite" (18-4).

hora = int(input("Digite a hora atual (0 a 23): "))

if 5 <= hora <= 11:
    print("Bom dia")
elif 12 <= hora <= 17:
    print("Boa tarde")
else:
    print("Boa noite")
