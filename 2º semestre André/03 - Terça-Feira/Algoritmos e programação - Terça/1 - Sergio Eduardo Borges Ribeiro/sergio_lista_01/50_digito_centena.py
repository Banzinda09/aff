# 50. Leia um número inteiro de 3 dígitos (ex: 382) e verifique se o dígito
#     das centenas é par ou ímpar (dica: use divisão inteira //).

numero = int(input("Digite um número inteiro de 3 dígitos: "))

digito_centena = numero // 100

if digito_centena % 2 == 0:
    print(f"O dígito das centenas ({digito_centena}) é par")
else:
    print(f"O dígito das centenas ({digito_centena}) é ímpar")
