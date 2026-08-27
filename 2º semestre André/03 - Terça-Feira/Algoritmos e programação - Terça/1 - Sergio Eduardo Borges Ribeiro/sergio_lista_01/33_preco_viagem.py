# 33. Peça a distância de uma viagem em km. Cobrar R$ 0.50 por km para viagens
#     até 200 km, e R$ 0.45 para viagens mais longas. Exiba o preço final.

distancia = float(input("Digite a distância da viagem (km): "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Preço final: R$ {preco:.2f}")
