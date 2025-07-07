mais_de_10 = 0
homens = 0
mulheres_menos_20 = 0

for c in range(4):
    idade = int(input(f"Digite a idade da {c+1}ª pessoa: "))
    sexo = input(f"Digite o sexo da {c+1}ª pessoa (M/F): ").strip().upper()
    
    if idade > 10:
        mais_de_10 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

print(f"\nQuantidade de pessoas com mais de 10 anos: {mais_de_10}")
print(f"Quantidade de homens cadastrados: {homens}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
