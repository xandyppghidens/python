op = int (input(" Qual operação voce quer ? (1 -> soma) (2 -> media)"))

num1 = int (input(" Digite um numero ? "))
num2 = int(input(" Digite o segundo numero ? "))

match(op):
      case 1:
            soma = num1 + num2

            print(" A soma é " + str(soma))

      case 2:
            media = num1 + num2 / 2
            print(" A media é " + str(media))

           