idade = int(input("Digite a sua idade: "))
genero = input("Digite o seu gênero (M para masculino / F para feminino): ").strip().upper()
if idade >= 18 and genero == "M":
    print("Candidato APTO para o alistamento militar.")
else:
    print("Candidato NÃO APTO para o alistamento militar.")