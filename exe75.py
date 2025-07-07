while True:
    numero = int(input("Digite um número para ver a tabuada (número negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado. Número negativo digitado.")
        break

    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()
