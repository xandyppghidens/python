peso = float(input(" Qual seu peso ? (em KG) "))

esc = int(input(" Escolha o planeta: \n 1 - Mercúrio \n 2 - Vênus \n 3 - Marte \n 4 - Júpiter \n 5 - Saturno \n 6 - Urano \n Digite o número do planeta: "))
match esc:
    case 1:
        marcurio = peso * 0.37
        
        print(" Seu peso em mercúrio é: ", marcurio, " kg ")
    case 2:
         venus = peso * 0.88
         print(" Seu peso em Vênus é: ", venus, " kg ")
    case 3:
        marte = peso * 0.38
        print(" Seu peso em Marte é: ", marte, " kg ")
    case 4:
        jupiter = peso * 2.64
        print(" Seu peso em Júpiter é: ", jupiter, " kg ")
    case 5:
        saturno = peso * 1.15
        print(" Seu peso em Saturno é: ", saturno, " kg ")
    case 6:
        urano = peso * 1.17
        print(" Seu peso em Urano é: ", urano, " kg ")
    case _:
        print("Opção inválida")





