idade = int(input("Informe a idade: "))

if idade < 6:
    tarifa = 0.00
elif (idade >= 6) and (idade < 18):
    tarifa = 5.00
elif (idade >= 18) and (idade < 60):
    tarifa = 10.00
else:
    tarifa = 0.00

print(f"Valor da tarifa: {tarifa}")