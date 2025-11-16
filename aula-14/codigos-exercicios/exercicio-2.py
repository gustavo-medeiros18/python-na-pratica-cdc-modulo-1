def calcular_velocidade_media(distancia, tempo):
    resultado = distancia / tempo
    resultado = round(resultado, 2)

    return resultado


dist = int(input("Informe a distância (km): "))
tempo = int(input("Informe o tempo (h): "))

vel_media = calcular_velocidade_media(dist, tempo)

print(f"Velocidade média: {vel_media} km/h")
