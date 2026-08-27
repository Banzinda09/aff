# 44. Receba uma data informada pelo usuário (dia, mês e ano separados) e
#     verifique se o mês é válido (entre 1 e 12).

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if 1 <= mes <= 12:
    print(f"Data {dia:02d}/{mes:02d}/{ano} - Mês válido")
else:
    print(f"Mês inválido: {mes}")
