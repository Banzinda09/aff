# 46. Crie um jogo de Pedra, Papel e Tesoura onde dois jogadores digitam suas
#     escolhas e o programa determina o vencedor ou empate.

jogador1 = input("Jogador 1, escolha (pedra/papel/tesoura): ").strip().lower()
jogador2 = input("Jogador 2, escolha (pedra/papel/tesoura): ").strip().lower()

opcoes_validas = ("pedra", "papel", "tesoura")

if jogador1 not in opcoes_validas or jogador2 not in opcoes_validas:
    print("Escolha inválida. Use: pedra, papel ou tesoura.")
elif jogador1 == jogador2:
    print("Empate!")
elif (
    (jogador1 == "pedra" and jogador2 == "tesoura")
    or (jogador1 == "papel" and jogador2 == "pedra")
    or (jogador1 == "tesoura" and jogador2 == "papel")
):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")
