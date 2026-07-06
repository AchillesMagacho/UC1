idade = int(input("Digite a sua idade: "))
genero = input("Você tem o ingresso? (responda com S para sim e N para não): ").strip().upper()
if idade >= 12 and genero == "S":
    print("Acesso liberado! Divirta-se no brinqueado.")
elif  idade <= 11 and genero == "S":
    print("Você tem o ingresso, mas não tem a idade mínima permitida")
else:
    print("Acesso negado. Você precisa de 1 ingresso")