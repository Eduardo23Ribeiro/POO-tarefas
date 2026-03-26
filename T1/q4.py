def somar_algarismos_frase(frase):
    soma = 0
    for numero in frase:
        if numero.isdigit():  
            soma += int(numero)
    return soma
numeros = somar_algarismos_frase(str(input("Digite a sequencia de numero")))
print(numeros)


