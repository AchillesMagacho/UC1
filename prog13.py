nome = input("Digite o seu nome: ")
nota2 = int(input("Digite o ano do nascimento: "))
media = 2026 - nota2
print(f"{nome} sua idade é {media}")
if media >= 18 and media <= 65:
    print("Maior de idade. Acesso liberado")
    print(f"Seja bem-vindo {nome}")
elif media >=65:
    print(f"seja bem vindo Sr.{nome}")
else:
    print("Menor de idade. Acesso negado")
