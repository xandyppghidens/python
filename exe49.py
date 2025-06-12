lados = []

for i in range(3):
    num = int(input(f"Digite o lado {i+1}: "))
    lados.append(num)

a, b, c = lados

if (a < b + c) and (b < a + c) and (c < a + b):
    print("É um triângulo")
else:
    print("Não é um triângulo")
    
if(a == b and b == c and c == a):
    print("É um triângulo equilátero")
   
if(a != b and b != c and c != a):
    print("É um triângulo escaleno")

if(a == b or b == c and c != a):
    print("É um triângulo isósceles")