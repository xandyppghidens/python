numero = int(input("Digite um número para ver a tabuada: "))

for c in range(1, 11):
    total = numero * c
    print(f"{numero} x {c} = {total}")