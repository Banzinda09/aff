numero = []
contador = 0
print('digite um numero positivo pra somar e quando quiser parar digite um numero negativo')

while contador >= 0:
    n = float(input(f'digite o numero {contador+1}: '))

    if n > 0:
        numero.append(n)
    contador += 1
    if n < 0:
        print(sum(numero))
        contador = -1