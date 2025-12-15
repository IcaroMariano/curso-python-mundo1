salario = float(input("Digite o salário: R$"))
if salario >= 1250:
    reajuste = salario * 1.1
else: 
    reajuste = salario * 1.15
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${reajuste:.2f}")