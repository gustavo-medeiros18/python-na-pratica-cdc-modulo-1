# atribuição inicial da senha
# cdc2025
senha = input("Informe a senha: ")

while senha != 'cdc2025':
    print("Senha incorreta! Tente novamente")
    senha = input("Informe a senha: ")

print("Senha correta. Fim do while")