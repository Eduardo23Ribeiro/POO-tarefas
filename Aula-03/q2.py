class Triangulo:
    def __init__(self):
        self.b = 0  #atributos
        self.h = 0
    def calc_area(self): #método
        return self.b * self.h /2
x = Triangulo() # chama o método
print(x.b, x.h)

x.b = float(input("Informe a altura do triangulo"))
x.h = float(input("Informe a base do triangulo"))

print(x.b,x.h)

a = x.calc_area()

print(f"A area do triangulo é {a:.2f}")

y = Triangulo()

print(y.b,y.h)

y.b = float(input("Informe a base do segundo triangulo"))
y.h = float(input("Informe a altura do segundo triangulo"))

print(y.b,y.h)

a = y.calc_area()
print(f"A area do segundo triangulo é {a:.2f}")