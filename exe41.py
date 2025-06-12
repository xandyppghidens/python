tempo_viagem = float(input("Informe o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Informe a velocidade média durante a viagem (em km/h): "))

distancia = tempo_viagem * velocidade_media

litros_usados = distancia / 12

print(f"\nTempo gasto na viagem: {tempo_viagem} horas")
print(f"Velocidade média: {velocidade_media} km/h")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Quantidade de litros usados: {litros_usados:.2f} litros")