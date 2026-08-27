# 36. Receba três notas, calcule a média ponderada (pesos 2, 3 e 5) e exiba se
#     a média é igual ou superior a 6.0.

nota1 = float(input("Digite a primeira nota (peso 2): "))
nota2 = float(input("Digite a segunda nota (peso 3): "))
nota3 = float(input("Digite a terceira nota (peso 5): "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

if media >= 6.0:
    print(f"Média ponderada: {media:.2f} - Aprovado")
else:
    print(f"Média ponderada: {media:.2f} - Reprovado")
