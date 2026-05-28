from datetime import datetime, timedelta
class treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    def set_id(self, id):
        if id < 0: raise ValueError("Ponha esse valor direito")
        self.__id = id

    def set_data(self, data):
        if data > datetime.now(): raise ValueError("a data não pode ser no futuro: ")
        self.__data = data

    def set_distancia(self, distancia):
        if distancia < 0: raise ValueError("Ponha o valor da distancia")
        self.__distancia = distancia

    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError("o tempo de treino não pode ser menor que 0")
        self.__tempo = tempo
    
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    
    def pace(self):
        p = self.__tempo / self.__distancia
        return p
    
    def __str__(self):
        return f"ID: {self.__id} - Data: {self.__data} - Distância: {self.__distancia} - Tempo: {self.__tempo}"
    

class treinoUI:
    __treinos = []

    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = treinoUI.menu()
            if op == 1: treinoUI.inserir()
            if op == 2: treinoUI.listar()
            if op == 3: treinoUI.listar_id()
            if op == 4: treinoUI.atualizar()
            if op == 5: treinoUI.excluir()
            if op == 6: treinoUI.maisrapido()

    @staticmethod
    def menu():
        print("1-inserir, 2-listar, 3-listar id, 4-atualizar, 5-excluir, 6-treino mais rápido")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("informe o id: "))
        data = datetime.strptime(input("informe a data do treino: "), "%d/%m/%Y")
        distancia = float(input("informe a distância percorrida: "))
        intervalo = input("digite o tempo no formato minutos:segunodos: ")
        m,s = map(int, intervalo.split(":"))
        tempo = timedelta(minutes=m, seconds=s)
        x = treino(id, data, distancia,tempo)
        cls.__treinos.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__treinos: print(x)

    @classmethod
    def listar_id(cls):
        for x in cls.__treinos: print(x.get_id())

    @classmethod
    def atualizar(cls):
        id = int(input("Selecione o treino que será atualizado: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                x.set_data(datetime.strptime(input("informe a data do treino: "), "%d/%m/%Y"))
                x.set_distancia(float(input("insira a distância: ")))
                intervalo = input("digite o tempo no formato minutos:segundos: ")
                m,s = map(int, intervalo.split(":"))
                tempo = timedelta(minutes=m, seconds=s)
                x.set_tempo(tempo)
            print("treino atulizado!")

    @classmethod
    def excluir(cls):
        id = int(input("informe o id do treino a ser excluído: "))
        for x in cls.__treinos:
            if x.get_id() == id:
               cls.__treinos.remove(x) 

    @classmethod
    def maisrapido(cls):
        mais_rapido = cls.__treinos[0]
        for x in cls.__treinos:
            if x.pace() < mais_rapido.pace():
                mais_rapido = x
        print(f"o treino mais rápido teve o pace de {mais_rapido.pace()}")


treinoUI.main()