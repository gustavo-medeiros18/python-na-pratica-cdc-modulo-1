#        0   1    2
tupla = (10, 20, 30)
print(f"Tipo da tupla: {type(tupla)}")

lista_convertida = list(tupla)








print(f"Tipo da lista convertida: {type(lista_convertida)}")
print(lista_convertida)

lista_convertida[1] = 2000
tupla = tuple(lista_convertida)

print(tupla)