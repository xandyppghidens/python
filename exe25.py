car = float(input(" Qual é a velocidade do carro ? "))

if(car <= 80):
       print(" Seguro ")

if(car >= 81 and car <=101):
       multa = 150.0
       cal = multa + 5
       print(" Limite de velocidade exedido ")

       print(" A multa é " + str(cal))

if(car >=101 and car <= 150):
        multa2 = 250.0
        cal2 = multa2 + 10

        print(" Limite de velocidade exedido ")
        print(" A multa é " + str(cal2))

if(car > 100 and car < 200):
       multa3 = 500.0
       cal3 = multa3 + 20
       print(" Limite de velocidade exedido ")
       print(" A multa é " + str(cal3))

if(car > 200):
       print(" Veiculo sera confiscado ")
