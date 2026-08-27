numeros = []
for i in range(2):
    n = float(input(f'digite o {i+1}º numero pra calcular a media: '))
    numeros.append(n)
resultado = sum(numeros) / len(numeros)
print(f'o resultado seria {resultado}')