def notas_aprovadas(lista_notas):
    lista_aprovados = []

    for nota in lista_notas:
        if nota >= 7.0:
            lista_aprovados.append(nota)

    return lista_aprovados


lista_notas_alunos = [10.0, 4.5, 7.5, 9.0]
lista_resultante = notas_aprovadas(lista_notas_alunos)

print("Notas aprovadas")
print(lista_resultante)