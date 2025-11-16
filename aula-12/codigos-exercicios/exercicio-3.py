# limite = 5
limite = int(input("Informe o limite: "))

# range(1, 6) -> [1, 2, 3, 4, 5]
# i = 1
# i = 2
# i = 3
# i = 4
# i = 5
for i in range(1, limite + 1):
    print(f"Dobro de {i}: {i * 2}")

print("Fim do for")