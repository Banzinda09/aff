# 48. Para os alunos "Em Recuperação" do exercício anterior, solicite a nota da
#     prova de recuperação e informe se a nova média ficou >= 5.0
#     ("Aprovado na Recuperação") ou não.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    print(f"Média: {media:.2f} - Aprovado")
elif media >= 5.0:
    print(f"Média: {media:.2f} - Em Recuperação")
    nota_recuperacao = float(input("Digite a nota da prova de recuperação: "))
    nova_media = (media + nota_recuperacao) / 2

    if nova_media >= 5.0:
        print(f"Nova média: {nova_media:.2f} - Aprovado na Recuperação")
    else:
        print(f"Nova média: {nova_media:.2f} - Reprovado")
else:
    print(f"Média: {media:.2f} - Reprovado")
