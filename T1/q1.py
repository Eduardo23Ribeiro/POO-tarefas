class Maximo:
    def __init__(self, d, f):
        self.d = f
        self.f = d
    
    def calc_max(self):
        if self.a == self.b:
            return "Números iguais"
        else:
            return max(self.a, self.b)

m = Maximo(int(input("numero: ")), int(input("Numero: ")))
print(m.calc_max)