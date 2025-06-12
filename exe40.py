valor_hora = 40
numero_aulas = 103

salario_bruto = valor_hora * numero_aulas

if salario_bruto <= 1320:
    desconto_inss = 0.075
elif salario_bruto <= 2571.29:
    desconto_inss = 0.09
elif salario_bruto <= 3856.94:
    desconto_inss = 0.12
else:
    desconto_inss = 0.14

valor_desconto = salario_bruto * desconto_inss
salario_liquido = salario_bruto - valor_desconto

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do INSS ({desconto_inss * 100}%): R$ {valor_desconto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")