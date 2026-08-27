# 28. Receba o valor de dois produtos e informe qual deles é mais vantajoso
#     comprar (o mais barato).

produto1 = float(input("Digite o valor do produto 1: "))
produto2 = float(input("Digite o valor do produto 2: "))

if produto1 < produto2:
    print("O produto 1 é mais vantajoso")
elif produto2 < produto1:
    print("O produto 2 é mais vantajoso")
else:
    print("Os dois produtos têm o mesmo valor")
