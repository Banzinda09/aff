# 22. Classifique um triângulo quanto aos lados: Equilátero (3 iguais),
#     Isósceles (2 iguais) ou Escaleno (3 diferentes).

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a == b == c:
    print("Triângulo Equilátero")
elif a == b or a == c or b == c:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")
