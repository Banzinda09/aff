# 20. Leia um caractere e informe se ele é uma vogal ou uma consoante
#     (considere apenas letras minúsculas).

caractere = input("Digite um caractere (letra minúscula): ")

if caractere in "aeiou":
    print("Vogal")
elif caractere.isalpha():
    print("Consoante")
else:
    print("Caractere inválido")
