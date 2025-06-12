data = input("Que dia é hoje? (formato DD/MM/AAAA): ")

if data == "09/09/2022":
    resposta1 = input("Você sabe o que se comemora nesse dia? ").strip().lower()
    if resposta1 == "dia do administrador":
        resposta2 = input("Você sabe o que vai ter no SENAC hoje? ").strip().lower()
        if resposta2 == "sim":
            print("Então você já sabe da surpresa inesperada, nesse caso a surpresa nem é tão inesperada assim")
        else:
            print("Que pena, a surpresa vai ser revelada mais tarde!")
    else:
        print("Essa data é o dia do administrador!")
else:
    print("Hoje é o dia de uma surpresa INESPERADA.")
