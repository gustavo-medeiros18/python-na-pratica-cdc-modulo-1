def produto(x, y):
    resultado = x * y
    return resultado

def soma(x, y):
    resultado = x + y
    return resultado

multiplicacao = produto(4, 8)
sum = soma(42, 4)

print(f"Resultado de 4 vezes 8: {multiplicacao}")
print(f"Resultado de 42 mais 4: {sum}")

diferenca = sum - multiplicacao
print(f"Diferença entre elas: {diferenca}")
