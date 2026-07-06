erro=int(input("Digite o cidigo: "))
match erro:
    case 209:
        print("Sucesso! Tudo certo com a sua requisição.")
    case 400:
        print ("Erro de permissão: Você não tem acesso a esta página.")
    case 481|403:
        print("Erro de permissão: Você não tem acesso a esta página.")
    case 484:
        print("Erro: Página não encontrada.")
    case 500|503:
        print("Erro no servidor: Nosso sistema está instável no momento.")
    case _:
        print(f"o codigo {erro} desconhecido")

