num1 = float(input(" Digite o primeiro número: "))
num2 = float(input(" Digite o segundo número: "))
num3 = float(input(" Digite o terceiro número: "))

if(num1 == num2 == num3):
    print("Os números são iguais. , É por isso não existe maior ou menor.")
    
else:
    menor =min(num1,num2,num3)
    maior =max(num1,num2,num3)
    print(f"O menor número é {menor} e o maior número é {maior}.")   
    
    numeros = [num1, num2 ,num3]
    numeros.sort()
    print(f"Os números em ordem do menor para o maior são: {numeros[0]} e {numeros[1]} e {numeros[2]}.")
    
    
    
    
    
    
    
    
    