from datetime import datetime, timedelta

class Treino:
    def __init__(self, data, id, distancia, tempo):
        self.set_data(data)
        self.set_id(id)
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    def set_data(self, v):
        if v > datetime.now():
            raise ValueError()
        self.__data = v

    def set_id(self, v):
        if v < 0:
            raise ValueError()
        self.__id = v

    def set_distancia(self, v):
        if v < float(0):
            raise ValueError()
        self.__distancia = v

    def set_tempo(self, v):
        if v.total_seconds() < 0:
            raise ValueError("Tempo inválido")
        self.__tempo = v
    def get_data(self):
        return self.__data
    def get_id(self):
        return self.__id
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def pace(self):
        if self.__distancia == 0:
            return "Distância não pode ser zero"
        pace_seconds = self.__tempo.total_seconds() / self.__distancia
        pace_minutes = int(pace_seconds // 60)
        pace_remaining_seconds = int(pace_seconds % 60)
        return f'Pace: {pace_minutes} min {pace_remaining_seconds} sec/km'

    def __str__(self):
        return f'ID: {self.__id}, Data: {self.__data.strftime("%d/%m/%Y")}, Distância: {self.__distancia} km, Tempo: {self.__tempo}'

class UI:
    __treinos = []

    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.listar_ID()
            if op == 4: UI.atualizar()
            if op == 5: UI.excluir()
            if op == 6: UI.pace()
    @staticmethod
    def menu():
        print("1 - Inserir Treino - 2 - Listar Treinos - 3 - Listar por ID - 4 - Atualizar Treino - 5 - Excluir Treino - 6 - Calcular Pace - 7 - Sair")
    @classmethod
    def inserir(cls):  
        id = int(input('id: '))
        data = datetime.strptime(input('data: '), "%d%m%y" )
        distancia = float(input('distancia: '))
        tempo_input = input('tempo (hh:mm:ss): ')
        x = Treino(id, data, distancia, tempo_input)

        cls.__treinos.append(x)
    @classmethod
    def listar(cls):
        