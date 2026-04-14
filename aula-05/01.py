# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
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

class Circulo:
    def __init__(self):
        self.__raio = 0.0
    def set_raio(self, v):
        if v >= 0: self.__raio = v
        else: raise ValueError()
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return (3.14 * self.__raio ) * 2
    def calc_circunferencia(self):
        return 


# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def triangulo():
        print("Cálculo da área do triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))     # método de instância
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")
    
    @staticmethod
    def circulo():
        print("Cálculo da área do Circulo")
        x = Circulo()
        x.set_raio(float(input("Informe o valor do raio: ")))
        area = x.calc_area()
        circunferencia = x.calc_circunferencia()
        print(f"Um circulo com raio {x.get_raio()}, tem area = {area} e circunferencia de {circunferencia}")

UI.main()