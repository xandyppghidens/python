a = float(input("Digite o primeiro número (A): "))
b = float(input("Digite o segundo número (B): "))
c = float(input("Digite o terceiro número (C): "))

if a == b and b == c:
    print("Os números são iguais, por isso não existe maior ou menor.")
else:
    numeros = [a, b, c]
    numeros.sort()  

    menor = numeros[0]
    meio = numeros[1]
    maior = numeros[2]

    print(f"Ordem do menor para o maior: {menor}, {meio}, {maior}")
    print(f"O número do meio é: {meio}")