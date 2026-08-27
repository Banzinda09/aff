# 27. Leia um ano e informe se ele é bissexto (divisível por 4 e não por 100,
#     ou divisível por 400).

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")
