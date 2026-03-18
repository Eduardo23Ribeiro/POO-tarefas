frase = input('frase: ')

recortes = frase.split()

for corte in recortes:
    
    frase_invertida = corte[::-1]
    print(frase_invertida)