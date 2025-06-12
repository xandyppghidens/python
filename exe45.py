nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

frequencia = float(input("Digite a frequência do aluno (em %): "))

if media >= 60 and frequencia > 75:
    print("Aprovado")

elif 40 <= media < 60:
    print("Está de recuperação")
    nota_recuperacao = float(input("Digite a nota da recuperação: "))
    if nota_recuperacao <= 69.99:
        print("Reprovado")
    else:
        print("Aprovado")

elif media < 40:
    print("Reprovado sem direito a recuperação")