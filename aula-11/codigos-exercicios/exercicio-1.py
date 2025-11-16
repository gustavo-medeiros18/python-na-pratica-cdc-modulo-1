temp = int(input("Informe a temperatura: "))

if temp >= 30:
    print("Está muito quente!")
elif (temp >= 20) and (temp < 30):
    print("Está agradável!")
else:
    print("Está muito frio!")