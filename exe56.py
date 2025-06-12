preco = float(input("Digite o preço do produto: R$ "))

print("\nEscolha a época do ano:")
print("[1] Carnaval")
print("[2] Férias escolares")
print("[3] Dia das Crianças")
print("[4] Black Friday")
print("[5] Natal")

opcao = int(input("Digite o número da opção: "))

match opcao:
    case 1:
        preco_final = preco * 1.10
        epoca = "Carnaval"
    case 2:
        preco_final = preco * 1.20
        epoca = "Férias escolares"
    case 3:
        preco_final = preco * 1.05
        epoca = "Dia das Crianças"
    case 4:
        preco_final = preco * 0.70
        epoca = "Black Friday"
    case 5:
        preco_final = preco * 0.95
        epoca = "Natal"
    case _:
        print("Opção inválida.")
        exit()

print(f"\nO preço final na época do {epoca} é R$ {preco_final:.2f}")
