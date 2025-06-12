lados = []

for i in range(3):
    num = int(input(f"Digite o lado {i+1}: "))
    lados.append(num)

a, b, c = lados

if (a < b + c) and (b < a + c) and (c < a + b):
    print("É um triângulo")
else:
    print("Não é um triângulo")
