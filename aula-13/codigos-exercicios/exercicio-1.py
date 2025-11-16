#            0         1         2
paises = ["Brasil", "Chile", "Holanda"]

print("Lista original")
print(paises)

paises.append("Argentina")

print("Após adicionar a Argentina")
print(paises)

paises.insert(1, "Espanha")

print("Após adicionar a Espanha")
print(paises)

paises.remove("Holanda")

print("Após remoção da Holanda")
print(paises)

paises.pop(2)

print("Após remoção do Chile")
print(paises)

print("Tamanho atual da lista de países")
print(len(paises))