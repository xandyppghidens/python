idade1 = int(input("Digite a idade da primeira pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

def categoria(idade):
    if idade <= 9:
        return "mirim"
    elif 10 <= idade <= 14:
        return "infantil"
    elif 15 <= idade <= 18:
        return "jovem"
    elif 19 <= idade <= 24:
        return "adulto"
    else:
        return "fora da categoria"

cat1 = categoria(idade1)
cat2 = categoria(idade2)

if cat1 == cat2 and cat1 != "fora da categoria":
    horario = input("As categorias são iguais. Qual será o horário da luta? ")
    print(f"Está marcado a luta de uma pessoa com {idade1} anos e outra pessoa com {idade2} anos na hora {horario}")
else:
    print("Luta cancelada")