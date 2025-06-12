car = float(input(" Qual é a velocidade do carro ? "))

if(car <= 80):
       print(" Seguro ")

if(car > 80):
       multa = 450.0
       cal = multa + 10
       print(" Limite de velocidade exedido ")

       print(" A multa é " + str(cal))
