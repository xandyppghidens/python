soma = 0
tentativas = 0

for c in range(9):
    numero = int(input(f"Digite o {c+1}º número (ou 999 para parar): "))
    if numero == 999:
        print("Programa finalizado pelo usuário.")
        break
    soma += numero
    tentativas += 1

print(f"\nForam feitas {tentativas} tentativas.")
print(f"A soma dos valores digitados é {soma}.")
