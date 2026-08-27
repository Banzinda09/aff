# 40. Peça a idade e o tempo de serviço de um trabalhador e informe se ele pode
#     se aposentar (Idade >= 65 ou Tempo de serviço >= 30 ou
#     (Idade >= 60 e Tempo >= 25)).

idade = int(input("Digite a idade do trabalhador: "))
tempo_servico = int(input("Digite o tempo de serviço (anos): "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("Pode se aposentar")
else:
    print("Ainda não pode se aposentar")
