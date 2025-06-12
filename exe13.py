num1 = int (input(" Digite o primeiro valor ? "))
num2 = int (input(" Digite o segundo valor ? "))
num3 = int (input(" Digite o terceiro valor ? "))

maioro = 0
if(num1 > 25):
    maioro = maioro + 1
if(num2 > 25):
    maioro = maioro + 1 
if(num3 > 25):
    maioro = maioro + 1

print(" Encontramos " + str(maioro) + " maior que 25")