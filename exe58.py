print("Escolha um humorista:")
print("[1] Fabio Porchat")
print("[2] Danilo Gentili")
print("[3] Rafinha Bastos")

opcao = int(input("Digite o número da opção: "))

cidade = input("Digite sua cidade: ").strip().lower()

match opcao:
    case 1:
        if cidade == "araxá" or cidade == "araxa":  # aceita com ou sem acento
            idade = int(input("Qual sua idade? "))
            if idade >= 18:
                print("Tem show do Fabio Porchat!")
            else:
                print("Não há show disponível para sua idade.")
        else:
            print("Sem shows disponíveis nessa cidade para Fabio Porchat.")

    case 2:
        if cidade == "são paulo" or cidade == "sao paulo":
            print("Tem show do Danilo Gentili!")
        else:
            print("Sem shows disponíveis nessa cidade para Danilo Gentili.")

    case 3:
        if cidade == "rio grande do sul":
            print("Tem show do Rafinha Bastos!")
        else:
            print("Sem shows disponíveis nessa cidade para Rafinha Bastos.")

    case _:
        print("Opção inválida.")
