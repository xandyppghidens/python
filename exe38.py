valor_produto = float(input("Digite o valor do produto: R$ "))

print("\nFormas de Pagamento:")
print("1 - À Vista em Dinheiro ou Pix (15% de desconto)")
print("2 - À Vista no cartão de crédito (10% de desconto)")
print("3 - Parcelado no cartão em 2x (sem juros)")
print("4 - Parcelado no cartão em 3x ou mais (10% de juros)")

codigo_pagamento = int(input("Digite o código da forma de pagamento (1 a 4): "))

if codigo_pagamento == 1:
    valor_final = valor_produto * 0.85
    descricao = "à vista em dinheiro ou Pix (15% de desconto)"
elif codigo_pagamento == 2:
    valor_final = valor_produto * 0.90
    descricao = "à vista no cartão de crédito (10% de desconto)"
elif codigo_pagamento == 3:
    valor_final = valor_produto
    descricao = "parcelado em 2x no cartão (sem juros)"
elif codigo_pagamento == 4:
    valor_final = valor_produto * 1.10
    descricao = "parcelado em 3x ou mais no cartão (com 10% de juros)"
else:
    print("Código inválido. Tente novamente.")
    exit()

print(f"\nForma de pagamento escolhida: {descricao}")
print(f"Valor final a ser pago: R$ {valor_final:.2f}")