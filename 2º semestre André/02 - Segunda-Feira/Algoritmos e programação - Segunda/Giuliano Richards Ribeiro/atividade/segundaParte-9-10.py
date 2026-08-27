#===== CADASTRO ===== 
#Nome: Maria 
#Idade: 22 anos
#Cidade: Belo Horizonte 
#Gosta de programar: Sim 
#===================== 
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
