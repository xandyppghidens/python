c = int(0)
mp = int(0)
ma = int(0)
while c != 5:
    nome = str(input(" Qual seu nome ? "))
    sex = str(input(" Qual seu sexo ? "))
    idade = int(input(" Qual sua idade ? "))
   
    if(idade > mp and sex == "m"):
        mp = mp +  idade

    if(idade < ma and sex == "f" ):
        ma = ma + idade

    c = c + 1
    print(f" O homem mais velho é {nome} com a idade {mp}")
    print(f" A mulher mais jovem é {nome} com a idade {ma}")

