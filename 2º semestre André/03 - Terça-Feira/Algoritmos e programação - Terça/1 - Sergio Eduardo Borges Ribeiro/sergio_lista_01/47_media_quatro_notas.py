# 47. Receba quatro notas de um aluno. Calcule a média. Se for >= 7.0
#     "Aprovado", entre 5.0 e 6.9 "Em Recuperação", e < 5.0 "Reprovado".

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.2f} - {situacao}")
