soma_pares = 0
soma_impares = 0
cont_pares = 0
cont_impares = 0

for c in range(4):
    numero = int(input(f"Digite o {c+1}º número: "))
    if numero % 2 == 0:
        print(f"{numero} é par")
        cont_pares += 1
        soma_pares += numero
    else:
        print(f"{numero} é ímpar")
        cont_impares += 1
        soma_impares += numero

soma_geral = soma_pares + soma_impares

print(f"\nForam cadastrados {cont_pares} números pares")
print(f"Foram cadastrados {cont_impares} números ímpares")
print(f"A soma dos pares é {soma_pares}")
print(f"A soma dos ímpares é {soma_impares}")
print(f"A soma geral é {soma_geral}")

