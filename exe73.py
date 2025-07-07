tentativas = 0

while True:
    numero = int(input("Digite um número: "))
    tentativas += 1

    if numero == 20:
        print("Você acertou! Número 20 digitado.")
        break

    if tentativas == 3:
        print("Número máximo de tentativas alcançado. Encerrando o programa.")
        break
