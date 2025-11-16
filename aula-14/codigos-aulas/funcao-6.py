# Variável no escopo global
meu_nome = "Isaac"

def exibir_nome():
    # Espaço do escopo local
    print(f"Seu nome é {meu_nome}")

exibir_nome()
len()
input()
round(2.45, 1)
# Escopo global NÂO ENXERGA o que está no escopo local
# Escopo local EXERGA o que está no escopo global