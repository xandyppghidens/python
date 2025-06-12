time = input("Qual time de futebol você torce? (Atlético ou Cruzeiro): ").strip().lower()

if time == "atletico" or time == "atletico":
    modelo = input("Qual uniforme você prefere? [modelo 1] ou [modelo 2]: ").strip()
    if modelo == "1":
        print("O valor será de R$85,00")
    elif modelo == "2":
        print("O valor será de R$75,00")
    else:
        print("Modelo inválido.")
        
elif time == "cruzeiro":
    modelo = input("Qual uniforme você prefere? [modelo 1] ou [modelo 2]: ").strip()
    if modelo == "1":
        print("O valor será de R$45,00")
    elif modelo == "2":
        print("O valor será de R$95,00")
    else:
        print("Modelo inválido.")
        
else:
    print("Time não reconhecido.")