num1 = int(input(" Digite um numero ? "))
num2 = int(input(" Digite um numero ? "))
num3 = int(input(" Digite um numero ? "))


soma1 = num1 + num2
soma2 = num2 + num3
soma3 = num1 + num3

if(soma1 > num3 and soma2 > num1 and soma3 > num2):
    print("É um triângulo")
else:
    print("Não é um triângulo")












