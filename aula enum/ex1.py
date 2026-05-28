import enum

class Estacao(enum.Enum):
    OUTONO = 1
    INVERNO = 2
    PRIMEVERA = 3
    VERAO = 4

a = Estacao.INVERNO
b = Estacao["VERAO"]
c = Estacao(3)
print(a)
print(b)
print(c)
print(a.name)
print(a.value)