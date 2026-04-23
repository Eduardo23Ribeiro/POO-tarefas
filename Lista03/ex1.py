class Retangulo:
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)

    def set_base(self, v):
        if v >= 0:
            self.base = v
        else:
            raise ValueError()

    def set_altura(self, v):
        if v >= 0:
            self.altura = v
        else:
            raise ValueError()

    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura

    def calc_area(self):
        return self.base * self.altura

    def __str__(self):
        return f"Base = {self.base} - Altura = {self.altura}"

class Frete:
    def __init__(self,d,p):
        self.set_distancia(d)
        self.set_peso(p)
    def set_distancia(self, v):
        if v >= 0:
            self.distancia = v
        else:
            raise ValueError()

    def set_peso(self, v):
        if v >= 0:
            self.peso = v
        else:
            raise ValueError()

    def get_distancia(self):
        return self.distancia


    def get_peso(self):
        return self.peso

    def calc_frete(self):
        return 0.01 * self.distancia * self.peso

    def __str__(self):
        return f"Peso = {self.peso}KG - distancia = {self.distancia}"
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.retangulo()
            if op == 2:
                UI.frete()
            if op == 3:
                UI.equacao()

    @staticmethod
    def menu():
        print("1 - Retângulo")
        print("2 - Frete")
        print("3 - Sair")
        return int(input("Informe uma opção: "))

    @staticmethod
    def retangulo():
        print("Cálculo da área do Retângulo")
        b = float(input("Informe a base: "))
        h = float(input("Informe a altura: "))
        
        x = Retangulo(b, h)
        area = x.calc_area()
        diagonal = (b**2 + h**2) ** 0.5
        
        print(x)
        print(f"Área = {area}, diagonal = {diagonal}")
    def frete():
        print("Cálculo da área do Retângulo")
        d = float(input("Informe a distancia: "))
        p = float(input("Informe o peso: "))
        
        x = Frete(d, p)
        frete = x.calc_frete()
        
        print(x)
        print(f"O valor do frete é {frete}")


UI.main()