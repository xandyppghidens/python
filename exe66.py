c = int(0)
mp = int(70)
mnp = int(9999)
while c !=4:
    peso = float(input(" Qual seu peso ? "))
    
    if(peso > mp ):
        mp = peso
    if(peso < mnp):
        mnp = peso
    if(peso == 70.0):
        print("peso normal")

    c = c + 1

print(" Existe pessoas acima do peso com " + str(mp) + " peso ")
print(" Existe pessoas abaixo do peso com " + str(mnp) + " peso ")



