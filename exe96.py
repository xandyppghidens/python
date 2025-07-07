av = [3 , 6 , 12 , 24 , 48 , 96 , 192 , 384 , 768 ,  1536]
c = int(0)

for c in range(10):
    if(c == 3 or c == 6 or c == 96):
         print(f"a dobra é ${c}$ , ")
    else: print(c)

print("------------------------------------")
numeros = [3 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
c2 = int(0)

for c2 in range(9):
     numeros[c2+1] = numeros[c2] * 2
     if(c2 == 3 or c2 == 6 or c2 == 96):
         print(f"a dobra é ${numeros[c2]}$ ")

     print(numeros[c2])






