
print("as operações vão de 1 a 4. 1 soma. 2 diminui. 3 multiplica e 4 dividi")
erro=int(input("EScolha 1 operação: "))
n1 = int(input("digite 1 numero "))
n2 = int(input("digite o segundo numero"))
match erro:
    case 1:
        final=n1 + n2
        print(f"o resultado é {final}")
    case 2:
        final2=n1 - n2
        print(f"o resultado é {final2}")
    case 3:
        final3=n1 * n2
        print(f"o resultado é {final3}")
    case 4:
        final4=n1/n2
        print(f"o resultado é {final4}")
    case _:
        print("numero desconhecido")

