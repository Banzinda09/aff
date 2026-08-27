# 15. Leia a nota de um aluno (0 a 10) e classifique: A (>= 9.0), B (>= 7.0),
#     C (>= 5.0) ou F (< 5.0).

nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 9.0:
    classificacao = "A"
elif nota >= 7.0:
    classificacao = "B"
elif nota >= 5.0:
    classificacao = "C"
else:
    classificacao = "F"

print(f"Classificação: {classificacao}")
