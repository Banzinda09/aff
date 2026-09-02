valor = float(input('qual seria o valor da sua compra: '))
desconto = float(input('qual seria o desconto da compra: '))
reais = desconto / 100
dindin = reais * valor
finalmente = valor - dindin
print(f'o valor da sua compra com o desconto de {desconto} seria {finalmente}')