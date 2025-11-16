# variável no escopo global
res = 100

def diferenca(x, y):
    # variável no escopo local
    res = x - y
    return res

diferenca(10, 4)
print(res)