#problema
#Idade = 15
#mensagem = "Você tem " + idade + " anos" 
#print(mensagem) 

#soluçao 1 alem da letra minuscula que tem que mudar e so colocar pro python str() 
# O problema é que o Python não sabe automaticamente como "juntar" um texto com um número usando + entao e so
# tranformar o numro em uma str()
Idade = 15
mensagem = "Você tem " + str(Idade) + " anos" 
print(mensagem) 

#soluçao 2 alem da letra minuscula que tem que mudar e tirar o " ao lados da idade colocando um F antes do " funciona
Idade = 15
mensagem = f"Você tem {Idade} anos" 
print(mensagem) 