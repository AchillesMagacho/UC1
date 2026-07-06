cargo = input("Digite a seu cargo (vendedor/caixa/gerente): ").strip().lower()
print("Não se preocupe o sistema já ira descontar o irrf e o inss ")
salario = 0
if cargo == "caixa":
    salario = 1500.0
elif cargo == "vendedor":
    salario = 2400.0
elif cargo == "gerente":
    salario = 4000.0
else:
    print("cargo invalido!")
inss = salario * 0.12
if salario > 2000.0:
    irrf = salario * 0.14
elif salario < 2000.0:
    irrf = salario * 0.08
final = salario - inss - irrf 
print(f"seu salairo burto é R${salario:.2f} já liquido é R${final:.2f}")