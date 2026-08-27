# 6. Receba duas notas de um aluno, calcule a média e exiba "Aprovado" se a média
#    for maior ou igual a 7.0, ou "Reprovado" se for menor.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f"Média: {media:.2f} - Aprovado")
else:
    print(f"Média: {media:.2f} - Reprovado")
