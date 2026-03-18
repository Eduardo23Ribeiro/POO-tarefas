frase = input('frase: ')

n = len(frase)
rotacao = frase

print("Frase Original:", frase)

for x in range(n):

    rotacao = rotacao[1:] + rotacao[0]

    print(rotacao)