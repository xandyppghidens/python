soma = 0
tentativas = 0

while True:
    numero = int(input("Digite um número (999 para parar): "))
    
    if numero == 999:
        break
    
    soma += numero
    tentativas += 1

print(f"\nVocê digitou {tentativas} números.")
print(f"A soma dos valores digitados é: {soma}")
