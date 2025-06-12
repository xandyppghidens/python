def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y

def main():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a opção (1/2/3/4): ")

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida.")
        return main()

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return main()

    if escolha == '1':
        print("Resultado:", add(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtract(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiply(num1, num2))
    elif escolha == '4':
        print("Resultado:", divide(num1, num2))

if __name__ == "__main__":
    main()