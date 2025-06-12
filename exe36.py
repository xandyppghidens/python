salario_antigo = float(input("Digite o valor do salário: R$ "))

reajuste = salario_antigo * 0.05
salario_novo = salario_antigo + reajuste

print(f"Seu salário antigo era R$ {salario_antigo:.2f} e agora com o reajuste é R$ {salario_novo:.2f}.")