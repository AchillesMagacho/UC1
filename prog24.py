print("As operações vão de 1 a 4. 1 soma. 2 diminui. 3 multiplica e 4 divide.")
operacao = int(input("Escolha 1 operação:  "))
n1 = int(input("Digite 1 número:  "))
n2 = int(input("Digite o segundo número:  "))
resultado = 0
match operacao:
    case 1:
        resultado = n1 + n2
    case 2:
        resultado = n1 - n2
    case 3:
        resultado = n1 * n2
    case 4:
        resultado = n1 / n2 if n2 != 0 else "Erro (divisão por zero)"
    case _:
     
        resultado = "Número desconhecido"

print(f"O resultado é: {resultado}")
print(f"O resultado do commit")