tentativas_nome = 0
tentativas_idade = 0

for c in range(3):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    erro_nome = nome != "João"
    erro_idade = idade <= 35
    
    if erro_nome:
        tentativas_nome += 1
        print("Nome incorreto.")
    if erro_idade:
        tentativas_idade += 1
        print("Idade incorreta.")
    
    if not erro_nome and not erro_idade:
        print("Dados corretos! Programa finalizado.")
        break
else:
    print("Bloqueado por excesso de tentativas erradas.")

print(f"\nTentativas de nomes errados: {tentativas_nome}")
print(f"Tentativas de idades erradas: {tentativas_idade}")
