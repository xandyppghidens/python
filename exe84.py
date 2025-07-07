for c in range(3):
    numero = int(input(f"Tentativa {c+1}: Digite um número: "))
    if numero == 20:
        print("Número 20 digitado. Programa finalizado.")
        break
else:
    print("Número 20 não foi digitado nas 3 tentativas.")
