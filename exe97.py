nota = [0,0,0,0,0,0]
c = int(0)
maior = int(0)
menor = int(999)
media = int(0)
for c in range(6):
  nota[c] = int(input(" Digite uma nota ? "))

  if(nota[c] > maior ):
      maior = nota[c]

  if(nota[c] < menor ):
     menor = nota[c]

  media = nota[c] / 6


print(f"A maior nota é {maior}")
print(f"A menor nota é {menor}")
print(f"A media é {media}")  
