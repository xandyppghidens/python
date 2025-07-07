usuario_correto = "fácil"
senha_correta = "ff"

multa = 2.00

while True:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso correto!")
        break
    else:
        print(f"Você será multado em R${multa:.2f} pela sua falha.")
        resposta = input("Gostaria de tentar novamente? (s/n): ").strip().lower()
        if resposta != 's':
            print("Você desistiu. Encerrando o programa.")
            break
        multa *= 2  
