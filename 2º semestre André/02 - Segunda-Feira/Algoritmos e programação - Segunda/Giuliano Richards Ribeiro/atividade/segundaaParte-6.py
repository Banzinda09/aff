#forma nutela que pode errar 1 ano
ano = int(input('escreva seu ano de nacimento: '))
idadereal = 2026 - ano
print(f'a sua idade aproximadamente seria {idadereal}')

#forma hacker boladao
import datetime

dia = int(input('escreva o dia do seu nascimento: '))
mes = int(input('escreva o mes do seu nascimento: '))
ano = int(input('escreva o ano do seu nascimento: '))

hoje = datetime.date.today()

idade_real = hoje.year - ano

if (mes, dia) > (hoje.month, hoje.day):
    idade_real -= 1

print(f'a sua idade real seria {idade_real}')