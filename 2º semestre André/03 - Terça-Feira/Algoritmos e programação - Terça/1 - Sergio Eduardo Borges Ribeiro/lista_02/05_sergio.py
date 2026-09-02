numero = []
contador = 0

while contador <= 4:
    n = float(input(f'digite o seu {contador + 1} numero: '))
    numero.append(n)
    contador += 1

resposta = sum(numero)
print(f'{resposta:.0f}')