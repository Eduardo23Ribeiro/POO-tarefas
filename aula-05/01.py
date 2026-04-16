class Triangulo:
    def __init__(self):
        self._b = 0.0
        self._h = 0.0

    def set_base(self, v):
        if v >= 0:
            self._b = v
        else:
            raise ValueError()

    def set_altura(self, v):
        if v >= 0:
            self._h = v
        else:
            raise ValueError()

    def get_base(self):
        return self._b

    def get_altura(self):
        return self._h

    def calc_area(self):
        return self._b * self._h / 2


class Circulo:
    def __init__(self):
        self._raio = 0.0

    def set_raio(self, v):
        if v >= 0:
            self._raio = v
        else:
            raise ValueError()

    def get_raio(self):
        return self._raio

    def calc_area(self):
        return 3.14 * (self._raio ** 2)

    def calc_circunferencia(self):
        return 2 * 3.14 * self._raio


class Viagem:
    def __init__(self):
        self._distancia = 0.0
        self._tempo = 0.0

    def set_distancia(self, d):
        if d >= 0:
            self._distancia = d
        else:
            raise ValueError()

    def set_tempo(self, t):
        if t > 0:
            self._tempo = t
        else:
            raise ValueError()

    def get_distancia(self):
        return self._distancia

    def get_tempo(self):
        return self._tempo

    def velocidade_media(self):
        return self._distancia / self._tempo


class ContaBancaria:
    def __init__(self):
        self._titular = ""
        self._numero = ""
        self._saldo = 0.0

    def set_titular(self, nome):
        self._titular = nome

    def set_numero(self, numero):
        self._numero = numero

    def get_titular(self):
        return self._titular

    def get_numero(self):
        return self._numero

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor

    def dados(self):
        return self._titular, self._numero, self._saldo


class Ingresso:
    def __init__(self):
        self._dia = ""
        self._hora = 0

    def set_dia(self, dia):
        self._dia = dia.lower()

    def set_hora(self, hora):
        self._hora = hora

    def get_dia(self):
        return self._dia

    def get_hora(self):
        return self._hora

    def valor_base(self):
        if self._dia in ["segunda", "terca", "quinta"]:
            return 16
        elif self._dia == "quarta":
            return 8
        elif self._dia in ["sexta", "sabado", "domingo"]:
            return 20

    def valor_ingresso(self):
        base = self.valor_base()
        if self._dia == "quarta":
            return base
        if 17 <= self._hora <= 23:
            base *= 1.5
        return base

    def meia_entrada(self):
        return self.valor_ingresso() / 2


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.triangulo()
            elif op == 2:
                UI.circulo()
            elif op == 3:
                UI.viagem()
            elif op == 4:
                UI.conta()
            elif op == 5:
                UI.ingresso()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def triangulo():
        x = Triangulo()
        x.set_base(float(input("Base: ")))
        x.set_altura(float(input("Altura: ")))
        print(x.calc_area())

    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input("Raio: ")))
        print(x.calc_area(), x.calc_circunferencia())

    @staticmethod
    def viagem():
        v = Viagem()
        v.set_distancia(float(input("Distância: ")))
        v.set_tempo(float(input("Tempo (h): ")))
        print(v.velocidade_media())

    @staticmethod
    def conta():
        c = ContaBancaria()
        c.set_titular(input("Nome: "))
        c.set_numero(input("Número: "))
        c.depositar(float(input("Depósito: ")))
        c.sacar(float(input("Saque: ")))
        print(c.dados())

    @staticmethod
    def ingresso():
        i = Ingresso()
        i.set_dia(input("Dia: "))
        i.set_hora(int(input("Hora: ")))
        print(i.valor_ingresso(), i.meia_entrada())


UI.main()