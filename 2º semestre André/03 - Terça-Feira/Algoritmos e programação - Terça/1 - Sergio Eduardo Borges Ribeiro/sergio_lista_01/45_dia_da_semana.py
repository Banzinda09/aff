# 45. Receba um número entre 1 e 7 e imprima o dia da semana correspondente
#     (1 = Domingo, 2 = Segunda, ..., 7 = Sábado).

numero = int(input("Digite um número entre 1 e 7: "))

dias = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado",
}

if numero in dias:
    print(dias[numero])
else:
    print("Número inválido")
