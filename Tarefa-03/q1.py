class Viagem:
    def __init__(self, des, dis, l):
        self.set_destino(des)
        self.set_distancia(dis)
        self.set_litros(l)

    def set_destino(self, destino):
        self.destino = destino

    def set_litros(self, litros):
        if litros >= 0:
            self.litros = litros
        else:
            raise ValueError("A quantidade de litros deve ser positiva.")

    def set_distancia(self, distancia):
        if distancia >= 0:
            self.distancia = distancia
        else:
            raise ValueError("A distância deve ser positiva.")

    def get_distancia(self):
        return self.distancia

    def get_destino(self):
        return self.destino

    def get_litros(self):
        return self.litros

    def calc_custo(self):
        return self.get_distancia() / self.get_litros()

    def __str__(self):
        return f"Destino: {self.destino}, Distância: {self.distancia}, Litros: {self.litros}"



class Pais:
    def __init__(self,nome,populacao,area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def set_nome(self,nome):
        if nome != "":
            self.nome = nome
        else:
            raise ValueError("O nome do país deve ser uma string não vazia.")

    def set_populacao(self,populacao):
        if populacao >= 0:
            self.populacao = populacao
        else:
            raise ValueError("A população deve ser um número inteiro positivo.")

    def set_area(self,area):
        if area >= 0:
            self.area = area
        else:            
            ValueError("A área deve ser positiva.")
    def get_nome(self):
        return self.nome
    def get_populacao(self):
        return self.populacao
    def get_area(self):
        return self.area
    def calc_densidade(self):
        return self.get_populacao() / self.get_area()
    def __str__(self):
        return f"Nome: {self.nome}, População: {self.populacao}, Área: {self.area}"

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1:
                UI.viagem()
            if op == 2:
                UI.paises()

    @staticmethod
    def menu():
        print("1 - Viagem")
        print("2 - Paises")
        print("3 - Sair")
        return int(input("Informe uma opção: "))

    @staticmethod
    def viagem():
        print("Cálculo do consumo da viagem")
        destino = input("Informe o destino: ")
        distancia = float(input("Informe a distância: "))
        litros = float(input("Informe a quantidade de litros: "))

        x = Viagem(destino, distancia, litros)
        custo = x.calc_custo()

        print(x)
        print(f"Consumo (km/l) = {custo:.2f}")
    @staticmethod
    def paises():
        print("Cálculo da densidade populacional do país")
        nome = input("Informe o nome do país: ")
        populacao = int(input("Informe a população: "))
        area = float(input("Informe a área: "))

        x = Pais(nome, populacao, area)
        densidade = x.calc_densidade()

        print(x)
        print(f"Densidade populacional (hab/km²) = {densidade:.2f}")


UI.main()