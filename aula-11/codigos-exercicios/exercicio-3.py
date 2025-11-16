username_correto = "admin"
senha_correta = "python2025"

username_entrada = input("username: ")
senha_entrada = input("senha: ")






if (username_entrada == username_correto) and (senha_entrada == senha_correta):
    print("login bem sucedido!")
else:
    print("credenciais incorretas!")