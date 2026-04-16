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
        return (self.__raio * 3.14) ** 2
    
    def calc_circunferencia(self):
        return (self.__raio * 2 * 3.14)

class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0

    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()

    def set_tempo(self, t):
        if t >= 0: self.__tempo = t
        else: raise ValueError()

    def get_distancia(self):
        return self.__distancia
    
    def get_tempo(self):
        return self.__tempo
    
    def velocidade_media(self):
        return self.__distancia / self.__tempo

class Conta_Bancaria:
    def __init__(self):
        self.__nome = str
        self.__num_conta = 0.0
        self.__saldo = 0.0

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_num_conta(self, v):
        if v >= 0: self.__num_conta = v
        else: raise ValueError()

    def get_num_conta(self):
        return self.__num_conta
    
    def set_saldo(self, v):
        if v >= 0: self.__saldo = v
        else: raise ValueError()

    def get_saldo(self):
        return self.__saldo
    
    def metodos(self, metodo, valor):
        if metodo == "d":
            self.__saldo += valor
            return valor

        elif metodo == "s":
            if valor <= self.__saldo:
                self.__saldo -= valor
                return valor

        else: raise ValueError()

class Ingresso:
    def __init__(self):
        self.__dia = str
        self.__horario = 0.0
    
    def set_dia(self, d):
        if d == 'segunda' or d == 'terça' or d == 'quarta' or d == 'quinta' or d == 'sexta' or d == 'sabado' or d == 'domingo':
            self.__dia = d
        else: raise ValueError()
    
    def get_dia(self):
        return self.__dia

    def set_horario(self, h):
        if 0 <= h <= 23:
            self.__horario = h
        else: raise ValueError()
    
    def get_horario(self):
        return self.__horario
    
    def calc_ingresso(self, idade):

        if 1 <= idade <= 18: 
            if self.__dia == 'segunda' or self.__dia == 'terça' or self.__dia == 'quinta':
                return f'R$ 8,00'
            
            elif self.__dia == 'quarta':
                return f'R$ 8,00'
            
            elif self.__dia == 'sexta' or self.__dia == 'sabado' or self.__dia == 'domingo':
                if self.__horario >= 17:
                    return f'R$ 15,00'
                else:
                    return f'R$ 10,00'
            
        elif 19 <= idade <= 200:
            if self.__dia == 'segunda' or self.__dia == 'terça' or self.__dia == 'quinta':
                return f'R$ 16,00'
            
            elif self.__dia == 'quarta':
                return f'R$ 8,00'
            
            elif self.__dia == 'sexta' or self.__dia == 'sabado' or self.__dia == 'domingo':
                if self.__horario >= 17:
                    return f'$ 30,00'
                else:
                    return f'R$ 20,00'

        else: raise ValueError()



# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta_bancaria()
            if op == 5: UI.ingresso()

    @staticmethod
    def menu():
        print("1-Triângulo, 2-Círculo, 3-Viagem, 4-Conta Bancária, 5-Ingresso, 9-Fim")
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
        print("="*40)

    @staticmethod
    def circulo():
        print("Cálculo da área e circunferencia do Circulo")
        x = Circulo()
        x.set_raio(float(input("Informe o valor da raio: ")))     # método de instância
        area = x.calc_area()
        circunferencia = x.calc_circunferencia()
        print(f"Um Circulo com raio {x.get_raio()}, tem área = {area}, e circunferencia = {circunferencia}")
        print("="*40)

    @staticmethod
    def viagem():
        print("Cálculo da Velocidade Media")
        x = Viagem()
        x.set_distancia(float(input("Informe o valor da distancia: ")))     # método de instância
        x.set_tempo(float(input("Informe o valor do tempo: ")))     # método de instância
        vel_med = x.velocidade_media()
        print(f"Uma Velocidade Media com distancia = {x.get_distancia()}, e tempo = {x.get_tempo()}. Tem Velocidade Media = {vel_med}km/h")
        print("="*40)

    @staticmethod
    def conta_bancaria():
        print("Conta Bancária")
        x = Conta_Bancaria()
        x.set_nome((input("Informe o seu Nome: ")))
        x.set_num_conta(float(input("Informe o Número da Conta: ")))     # método de instância
        x.set_saldo(float(input("Informe o seu Saldo: ")))
        operacao = input('Digite "d" para DEPOSITO ou "s" para SAQUE: ').lower().strip()
        valor = float(input("Digite o valor: "))     # método de instância
        metodos = x.metodos(operacao, valor)
        print(f"Conta Bancaria de {x.get_nome()}, tem numero de conta: {x.get_num_conta()}, Saldo Antigo: {x.get_saldo():.2f}\n Novo Valor Bancario = {metodos:.2f}")
        print("="*40)

    @staticmethod
    def ingresso():
        print("Ingressos")
        x = Ingresso()
        x.set_dia((input("Informe o dia: ")))     # método de instância
        x.set_horario(float(input("Informe o horario: ")))     # método de instância
        idade = float(input("Digite a sua Idade: "))
        calculo_ingresso = x.calc_ingresso(idade)
        print(f"Seu Ingresso que é do dia: {x.get_dia()}, e tem horario às: {x.get_horario()}. Sai pelo valor de: {calculo_ingresso}")
        print("="*40)    

UI.main()