import random

derrotas = 0

for c in range(1000):  
    numero_usuario = int(input("Digite um número de 1 a 10: "))
    escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()
    
    numero_sorteado = random.randint(1, 9)
    soma = numero_usuario + numero_sorteado
    
    resultado = "PAR" if soma % 2 == 0 else "IMPAR"
    
    print(f"Você jogou {numero_usuario} e o computador {numero_sorteado}. Total: {soma} => {resultado}")
    
    if (resultado == "PAR" and escolha == "P") or (resultado == "IMPAR" and escolha == "I"):
        print("Você GANHOU!")
        break
    else:
        print("Você PERDEU!\n")
        derrotas += 1

print(f"Total de derrotas antes da vitória: {derrotas}")
