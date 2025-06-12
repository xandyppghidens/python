a = str(input(" Qual serie voce viu essa semana ? "))

esc = int(input(" Escolha a opção: \n 1 - A série é de ação \n 2 - A série é de comédia \n 3 - A série é de drama \n 4 - A série é de terror \n 5 - A série é de ficção científica \n Digite o número da opção: "))
match esc:
    case 1:
        print(f"Você viu a série {a} Sandman")
    case 2:
        print(f"Você viu a série {a} Wandinha.")
    case 3:
        print(f"Você viu a série {a} Game of Thrones.")
    case 4:
        print(f"Você viu a série {a} Dota. ")
    case 5:
        print(f"Você viu a série {a} Dexter. ")
    case _:
        print("Opção inválida.")



