letras = {
    "a": "a",
    "b": "bac",
    "c": "cad",
    "d": "def",
    "e": "e",
    "f": "feg",
    "g": "geh",
    "h": "hij",
    "i": "i",
    "j": "jik",
    "k": "kil",
    "l": "lim",
    "m": "mon",
    "n": "nop",
    "o": "o",
    "p": "poq",
    "q": "qor",
    "r": "ros",
    "s": "sut",
    "t": "tuv",
    "u": "u",
    "v": "vuw",
    "w": "wux",
    "x": "xuy",
    "y": "yuz",
    "z": "zuz" 
}

def textos(texto):
    palavrafinal = ""
    for letra in texto:
        if letra in letras:
            palavrafinal += letras[letra]
        else:
            palavrafinal += letra
    return palavrafinal
print(textos("arteiro"))