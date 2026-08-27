# 24. Receba a idade de uma pessoa e informe se ela é Criança (0-12),
#     Adolescente (13-17), Adulto (18-59) ou Idoso (>= 60).

idade = int(input("Digite a idade: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade inválida")
