faixa1 = 0  # [0-25]
faixa2 = 0  # [26-50]
faixa3 = 0  # [51-75]
faixa4 = 0  # [76-100]

while True:
    try:
        numero = int(input("Digite um número entre 0 e 100: "))
        
        if 0 <= numero <= 25:
            faixa1 += 1
        elif 26 <= numero <= 50:
            faixa2 += 1
        elif 51 <= numero <= 75:
            faixa3 += 1
        elif 76 <= numero <= 100:
            faixa4 += 1
        else:
            print("Número fora do intervalo [0-100], não será contado.")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar == 's':
            True
            
        if(continuar == 'n'):
            break

    except ValueError:
        print("Por favor, digite um número válido.")

print("\nRESULTADO FINAL:")
print(f"Números entre [0-25]: {faixa1}")
print(f"Números entre [26-50]: {faixa2}")
print(f"Números entre [51-75]: {faixa3}")
print(f"Números entre [76-100]: {faixa4}")
