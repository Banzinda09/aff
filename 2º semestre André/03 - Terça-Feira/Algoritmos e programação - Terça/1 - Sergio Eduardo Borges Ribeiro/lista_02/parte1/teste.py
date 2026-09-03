notas = []
contador = 1
n = 0                          # valor inicial só pra passar na 1ª verificação

while n >= 0:
    n = float(input(f'digite sua {contador}ª nota: '))
    if n >= 0:
        notas.append(n)
        contador += 1

media = sum(notas) / len(notas)
print(f'a media das suas notas e {media:.2f}')