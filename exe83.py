homens = 0

for c in range(3):
    nome = input(f"Digite o nome da {c+1}ª pessoa: ")
    sexo = input(f"Digite o sexo de {nome} (M/F): ").strip().upper()
    
    if sexo == 'M':
        homens += 1

print(f"\nForam cadastrados {homens} homens.")
