v=int(input("Digite a temperatura "))
if v < 18:
    print("O clima está frio") 
elif v >= 18 and v <= 30:
    print("O clima está agradavel") 
elif v > 30:
    print("O clima está quente")
else:
    print("clima indisponivel")