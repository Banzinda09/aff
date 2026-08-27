# 18. Leia o turno em que o aluno estuda ("M" para Matutino, "V" para Vespertino,
#     "N" para Noturno) e exiba uma mensagem de saudação apropriada.

turno = input("Digite o turno (M/V/N): ").strip().upper()

if turno == "M":
    print("Bom dia, aluno do turno Matutino!")
elif turno == "V":
    print("Boa tarde, aluno do turno Vespertino!")
elif turno == "N":
    print("Boa noite, aluno do turno Noturno!")
else:
    print("Turno inválido")
