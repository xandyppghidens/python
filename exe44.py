from datetime import date

vendas = float(input("Quanto você vendeu neste mês? R$ "))

if vendas >= 22000:
    ano_entrada = int(input("Em que ano você entrou na empresa? "))
    ano_atual = date.today().year
    tempo_empresa = ano_atual - ano_entrada

    if tempo_empresa == 2:
        comissao = vendas * 0.03
    elif tempo_empresa >= 3:
        comissao = vendas * 0.04
    else:  
        comissao = vendas * 0.02

    print(f"Sua comissão será de R$ {comissao:.2f}")
else:
    print("Você não atingiu a meta mínima de R$22.000,00, portanto, sem comissão.")