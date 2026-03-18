def RemoverEspacos(texto):
    
    recortes = texto.split()
    frase = "".join(recortes)
    texto = frase[::1]
    return texto

print(RemoverEspacos("SIX OF THE KING OF THE POWE AND SEVEN OF THE KING OF THE POWER"))