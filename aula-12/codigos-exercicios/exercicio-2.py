# limite = 5
limite = int(input("Informe o limite: "))
# produtorio = 1
# produtorio = 1
# produtorio = 2
# produtorio = 6
# produtorio = 24
# produtorio = 120
produtorio = 1

# range(1, 6) -> [1, 2, 3, 4, 5]
# i = 1
# i = 2
# i = 3
# i = 4
# i = 5
for i in range(1, limite + 1):
    produtorio = produtorio * i

print(f"Resultado produtório: {produtorio}")