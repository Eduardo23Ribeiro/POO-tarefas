import math

class Retangulo:

    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)

    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()

    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()

    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h
    
    def calc_area(self):
        return self.__b * self.__h / 2
    
    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** (1/2)

    def __str__(self):
        return f"Base = {self.__b}, Altura = {self.__h}"
    
class Frete:

    def __init__(self, d, p):
        self.set_distancia(d)
        self.set_peso(p)

    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()

    def set_peso(self, v):
        if v >= 0: self.__p = v
        else: raise ValueError()

    def get_base(self):
        return self.__d
    
    def get_altura(self):
        return self.__p
    
    def calc_frete(self):
        return 0.01 * self.__d * self.__p

    def __str__(self):
        return f"Peso = {self.__d}Kg, Distancia = {self.__p}Km"
    
class Equa:

    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
    
    def set_a(self, v):
        if v == 0: raise ValueError()
        self.__a = v

    def set_b(self, v):
        self.__b = v

    def set_c(self, v):
        self.__c = v

    def get_a(self): return self.__a
    def get_b(self): return self.__b
    def get_c(self): return self.__c

    def calc_delta(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    def tem_raizes_reais(self):
        return self.calc_delta() >= 0
    
    def raiz_1(self):
        if not self.tem_raizes_reais():
            return "Não existem raízes reais"
        d = self.calc_delta()
        return ( - self.__b + math.sqrt(d)) / (2 * self.__a)

    def raiz_2(self):
        if not self.tem_raizes_reais():
            return "Não existem raízes reais"
        d = self.calc_delta()
        return ( - self.__b - math.sqrt(d)) / (2 * self.__a)

    def __str__(self):
        return f"Equação: {self.__a}x² + {self.__b}x + {self.__c} = 0"

    
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.retangulo()
            if op == 2: UI.frete()
            if op == 3: UI.equa()

    @staticmethod
    def menu():
        print("1 - Retangulo")
        print("2 - Frete")
        print("3 - Equação")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def retangulo():
        print("Cálculo da área e da diagonal do retangulo")
        b = (float(input("base: ")))
        h = (float(input("altura: ")))
        x = Retangulo(b, h)
        area = x.calc_area()
        diagonal = x.calc_diagonal()
        print(x)
        print(f"Um Retangulo tem Área: {area}, e Diagonal: {diagonal} ")
        print("="*100)
    
    @staticmethod
    def frete():
        print("Cálculo do Frete")
        d = (float(input("distancia: ")))
        p = (float(input("peso: ")))
        x = Frete(d, p)
        frete = x.calc_frete()
        print(x)
        print(f"Um Frete cujo valor total é: {frete} Reais")
        print("="*100)

    @staticmethod
    def equa():
        print("Cálculo da Equação")
        a = (float(input("A: ")))
        b = (float(input("B: ")))
        c = (float(input("C: ")))
        x = Equa(a, b, c)
        delta = x.calc_delta()
        raiz1 = x.raiz_1()
        raiz2 = x.raiz_2()
        print(x)
        print(f"Uma Equação cujas Raizes são: {raiz1}, {raiz2}. Tem delta: {delta} ")
        print("="*100)

UI.main()