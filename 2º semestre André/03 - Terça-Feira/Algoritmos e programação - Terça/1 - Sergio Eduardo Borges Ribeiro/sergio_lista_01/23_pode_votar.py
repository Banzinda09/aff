# 23. Receba o ano de nascimento de uma pessoa e informe se ela já pode votar
#     (idade >= 16).

ANO_ATUAL = 2026
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ANO_ATUAL - ano_nascimento

if idade >= 16:
    print("Já pode votar")
else:
    print("Ainda não pode votar")
