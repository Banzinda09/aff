# 49. Receba as coordenadas (X, Y) de um ponto no plano cartesiano e determine
#     em qual quadrante ele se encontra (Q1, Q2, Q3, Q4) ou se está sobre um
#     dos eixos/origem.

x = float(input("Digite a coordenada X: "))
y = float(input("Digite a coordenada Y: "))

if x == 0 and y == 0:
    print("O ponto está na origem")
elif x == 0:
    print("O ponto está sobre o eixo Y")
elif y == 0:
    print("O ponto está sobre o eixo X")
elif x > 0 and y > 0:
    print("O ponto está no Quadrante Q1")
elif x < 0 and y > 0:
    print("O ponto está no Quadrante Q2")
elif x < 0 and y < 0:
    print("O ponto está no Quadrante Q3")
else:
    print("O ponto está no Quadrante Q4")
