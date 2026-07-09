n1 = int(input("Digite 1 número :  "))
numero = n1
print(f"Tabuada do {numero}:")
print("----------------------")
for i in range(1, 11):
    r = numero * i
    print(f"{numero} x {i} = {r}")