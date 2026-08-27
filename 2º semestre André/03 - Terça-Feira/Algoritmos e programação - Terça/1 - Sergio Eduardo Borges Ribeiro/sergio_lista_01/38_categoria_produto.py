# 38. Receba um código de produto (1 a 4) e informe a sua categoria
#     (1: Alimento, 2: Eletrônico, 3: Vestuário, 4: Limpeza).
#     Se for outro código, exiba "Código inválido".

codigo = int(input("Digite o código do produto (1 a 4): "))

if codigo == 1:
    print("Categoria: Alimento")
elif codigo == 2:
    print("Categoria: Eletrônico")
elif codigo == 3:
    print("Categoria: Vestuário")
elif codigo == 4:
    print("Categoria: Limpeza")
else:
    print("Código inválido")
