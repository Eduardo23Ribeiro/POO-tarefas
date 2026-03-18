frase = input('frase: ')

recortes = frase.split()

while len(recortes) > 0:

    frase_atual = " ".join(recortes)
    print(frase_atual)

    recortes = recortes[1:]