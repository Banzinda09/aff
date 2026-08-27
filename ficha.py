nome = str(input('qual e o seu nome: '))
idade = int(input('qual e sua idade: '))
cidade = str(input('qual e sua cidade: '))
py = input('voce gosta de programar: ')
python = py.upper()
if python == 'SIM':
    like = True
else:
    like = False

print('===== CADASTRO ===== ')
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Cidade: {cidade}')
print(f'Gosta de programar: {like}')
print('=====================')

#confirmaçao
#qual e o seu nome: a
#qual e sua idade: 1
#qual e sua cidade: a
#voce gosta de programar: sim
#===== CADASTRO ===== 
#Nome: a
#Idade: 1 anos
#Cidade: a
#Gosta de programar: True
#=====================
#(projeto_aula1) PS C:\Users\André Dornelas\OneDrive\Área de Trabalho\python codes> 