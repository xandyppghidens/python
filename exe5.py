div = float (input(" Qual sua divida ? "))

time = int (input(" Qual o tempo dessa divida ? "))

juros = float (input(" Qual é a taxa de juros ? "))

totalj = div * time * juros

total = div + totalj

print(" Os juros são " + str(totalj) + " é o total sera de " + str(total))