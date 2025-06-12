id1 = int(input(" Quantos anos voce tem ? "))
id2 = int(input(" Quantos anos voce tem ? "))
id3 = int(input(" Quantos anos voce tem ? "))
id4 = int(input(" Quantos anos voce tem ? "))

menor = int(9999)
maior = int(0)

if(id1 > maior):
    maior = id1

if(id1 < menor):
    menor = id1

if(id2 > maior):
    maior = id2

if(id2 < menor):
    menor = id2

if(id3 > maior):
    maior = id3

if(id3 < menor):
    menor = id3

if(id4 > maior):
    maior = id4

if(id4 < menor):
    menor = id4

print(" O maior é " + str(maior))
print(" O menor é " + str(menor))