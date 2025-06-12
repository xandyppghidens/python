distancia = float(input("Qual a distância da corrida (em km)? "))

if distancia <= 200:
    preco_por_km = 0.35
else:
    preco_por_km = 0.20

valor_base = distancia * preco_por_km

perigoso = input("O bairro de destino é perigoso? (sim/não) ").strip().lower()

if perigoso == "sim":
    if distancia <= 200:
        valor_final = valor_base * 2
    else:
        valor_final = valor_base * 1.8
else:
    valor_final = valor_base

print(f"O valor final da corrida para o destino escolhido é R$ {valor_final:.2f} reais.")
