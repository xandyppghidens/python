print("Seu conhecimento de Excel é:")
print("[1] Básico")
print("[2] Intermediário")
print("[3] Avançado")
nivel = int(input("Escolha uma opção: "))

match nivel:
    case 1:
        print("\nPara que serve as fórmulas:")
        print("[1] SOMA")
        print("[2] MÉDIA")
        print("[3] MÁXIMO")
        escolha = int(input("Escolha uma opção: "))
        match escolha:
            case 1:
                print("A função SOMA serve para somar valores em um intervalo de células.")
            case 2:
                print("A função MÉDIA calcula a média aritmética dos valores selecionados.")
            case 3:
                print("A função MÁXIMO retorna o maior valor de um intervalo.")
            case _:
                print("Opção inválida.")

    case 2:
        print("\nPara que serve as fórmulas:")
        print("[1] SE")
        print("[2] SOMASE")
        print("[3] CONT.SE")
        escolha = int(input("Escolha uma opção: "))
        match escolha:
            case 1:
                print("A função SE executa um teste lógico e retorna um valor se for verdadeiro ou outro se for falso.")
            case 2:
                print("A função SOMASE soma os valores que atendem a um critério específico.")
            case 3:
                print("A função CONT.SE conta quantas vezes um valor atende a um critério.")
            case _:
                print("Opção inválida.")

    case 3:
        print("\nPara que serve as fórmulas:")
        print("[1] ORDEM.EQ")
        print("[2] PROCV")
        print("[3] PROCH")
        escolha = int(input("Escolha uma opção: "))
        match escolha:
            case 1:
                print("A função ORDEM.EQ retorna a posição de um número em uma lista de acordo com sua ordem.")
            case 2:
                print("A função PROCV procura um valor na primeira coluna de uma tabela e retorna um valor na mesma linha de outra coluna.")
            case 3:
                print("A função PROCH procura um valor na primeira linha de uma tabela e retorna um valor na mesma coluna de outra linha.")
            case _:
                print("Opção inválida.")

    case _:
        print("Nível de conhecimento inválido.")
