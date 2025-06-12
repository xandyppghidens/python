casa = float(input(" Qual é o valor da casa ? "))
s = float (input(" Qual é o seu salario ? "))
meses = int(input(" Em quantos meses voce vai pagar ? "))

cl = meses * casa < 0.3

if(s < cl):
     print(" Acesso a compra negado ")

else: print(" Compra ok ")