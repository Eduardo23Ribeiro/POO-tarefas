def somar_algarismos_frase(frase):
    soma = 0
    for caractere in frase:
        if caractere.isdigit():  
            soma += int(caractere)
    return soma
frase_principal = somar_algarismos_frase(str(input("Digite uma frase")))
print(frase_principal)


