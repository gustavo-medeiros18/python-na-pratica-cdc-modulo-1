media = float(input("Média do aluno: "))

if media >= 7.0:
    print("Passou direto!")
elif (media >= 4.0) and (media < 7.0):
    print("Recuperação.")

    nota_rec = float(input("Nota de recuperação: "))

    if nota_rec >= 7.0:
        print("Passou na recuperação.")
    else:
        print("Reprovou na recuperação.")
else:
    print("Reprovou direto.")