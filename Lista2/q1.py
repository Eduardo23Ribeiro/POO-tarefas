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


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.retangulo()

    @staticmethod
    def menu():
        print("1 - Retângulo")
        print("9 - Sair")
        return int(input("Informe uma opção: "))

    @staticmethod
    def retangulo():
        print("Cálculo da área do Retângulo")
        b = float(input("Informe a base: "))
        h = float(input("Informe a altura: "))
        
        x = Retangulo(b, h)
        area = x.calc_area()
        
        print(x)
        print(f"Área = {area}")



UI.main()