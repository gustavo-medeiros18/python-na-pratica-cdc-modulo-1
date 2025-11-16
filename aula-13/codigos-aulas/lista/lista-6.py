# pop(posicao)
#         0      1        2
lista = [2.54, False, "caneta"]
print(f"Tipo da lista: {type(lista)}")

print("Lista antes do pop")
print(lista)
tam = len(lista)
print(f"Tamanho da lista: {tam}")

lista.pop(1)

print("Lista após o pop")
print(lista)
tam = len(lista)
print(f"Tamanho da lista: {tam}")
