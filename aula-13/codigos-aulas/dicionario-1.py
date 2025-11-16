dicionario = {
    "nome": "Gustavo",
    "estado": "Ceará",
    "altura": 1.73
}

print(f"Tipo do dicionário: {type(dicionario)}")

print("Dicionário antes da modificação")
print(dicionario)

dicionario["nome"] = "Dev Gustavo"
dicionario["linguagem"] = "Python"

print("Dicionário após a modificação")
print(dicionario)

print(dicionario["nome"])
print(dicionario["estado"])
