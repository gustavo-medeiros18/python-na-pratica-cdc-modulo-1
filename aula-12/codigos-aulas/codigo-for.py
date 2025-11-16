

# somatorio = 0
# sequencia: [1, 2, 3, 4, 5]
# i = 1
# somatorio = 0 + 1 -> 1
# i = 2
# somatorio = 1 + 2 -> 3
# i = 3
# somatorio = 3 + 3 -> 6
# i = 4
# somatorio = 6 + 4 -> 10
# i = 5
# somatorio = 10 + 5 -> 15
somatorio = 0
for i in range(1, 6):
    print(f"Executando pela {i}a vez")
    # somatorio = somatorio + i
    # somatorio += i
    # somatorio = somatorio - i
    # somatorio -= i

print(f"Somatorio dos numeros: {somatorio}")
print("Acabou o loop")