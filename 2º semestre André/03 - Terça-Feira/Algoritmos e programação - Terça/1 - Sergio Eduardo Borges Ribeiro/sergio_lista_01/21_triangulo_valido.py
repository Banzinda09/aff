# 21. Solicite três lados de um triângulo e verifique se eles formam um
#     triângulo válido (a soma de dois lados deve ser sempre maior que o terceiro).

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os lados formam um triângulo válido")
else:
    print("Os lados NÃO formam um triângulo válido")
