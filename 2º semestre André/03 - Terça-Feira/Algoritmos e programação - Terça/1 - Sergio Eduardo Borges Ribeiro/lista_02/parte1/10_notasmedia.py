notas = []
contador = 1

while contador >= 0:
    n = float(input(f'digite sua {contador} nota: '))
    if n >= 0:
        notas.append(n)
        contador += 1
    if n < 0:
        media = sum(notas) / len(notas)
        print(f'a media das suas notas e {media:.2f}')
        contador = -1