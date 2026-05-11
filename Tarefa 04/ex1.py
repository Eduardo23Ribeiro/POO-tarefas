class time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Põe um nome aí seu bocó")
        self.__nome = nome 

    def set_estado(self, estado):
        if estado == "":
            raise ValueError("Põe o nome do estado aí seu bobão")
        self.__estado = estado

    def set_id(self, id):
        if id < 0:
            raise ValueError("O seu id deve ser positivo")
        self.__id = id

    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f"time {self.__nome} - estado {self.__estado} - id {self.__id}"
    
class jogador:
    def __init__(self, id, nome, idtime, camisa):
        self.set_id(id)
        self.set_nome(nome)
        self.set_idtime(idtime)
        self.set_camisa(camisa)
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Põe um nome aí seu bocó")
        self.__nome = nome 
    
    def set_id(self, id):
        if id < 0:
            raise ValueError("O seu id deve ser positivo")
        self.__id = id

    def set_idtime(self, idtime):
        if idtime < 0:
            raise ValueError("O seu id deve ser positivo")
        self.__idtime = idtime
    
    def set_camisa(self, camisa):
        if camisa < 0:
            raise ValueError("tem que ser maior que zero papai")
        self.__camisa = camisa
    
    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id
    def get_idtime(self):
        return self.__idtime
    def get_camisa(self):
        return self.__camisa
    
    def __str__(self):
        return f"nome do jogador: {self.__nome} - id do jogador: {self.__id} - idTime: {self.__idtime} - camisa: {self.__camisa}"
    
class UI:
    times = []
    jogadores = []
    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_time()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_time()
            if op == 5: UI.inserir_jogador()
            if op == 6: UI.listar_jogador()
            if op == 7: UI.atualizar_jogador()
            if op == 8: UI.excluir_jogador()
            if op == 9: UI.listar_jogador_do_time()
            if op == 10: UI.transferir_jogador()

    @staticmethod
    def menu():
        print("1-Inserir time, 2-Listar time, 3-Atualizar time, 4-Excluir time, 5-inserir jogadores, 6-listar jogadores, 7-atualizar jogadores, 8-excluir jogadores, 9-listar jogadores, 10-transferir jogador ")
        return int(input("escolha uma opção: "))
    
    @classmethod
    def inserir_time(cls):
        id = int(input("informe o id do time: "))
        nome = input("informe o nome: ")
        estado = input("informe o estado do seu time: ")
        x = (id, nome, estado)
        cls.times.append(x)
        print("Time inserido com sucesso")
    
    @classmethod
    def listar_time(cls):
        if len(cls.times) == 0: print("Nenhum time listado")
        else:
            for x in cls.times: print(x)

    @classmethod
    def listar_id(cls, id):
        #procurar um item com o id informado
        for x in cls.times:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar_time(cls):
        UI.listar_time()
        id = int(input('informe o id do time a ser alterado'))
        x = UI.listar_id(id)
        if x != None:
            #remove o contato atual
            cls.times.remove(x)
            #insere um novo contato com os dados atualizados
        nome = input("informe o nome: ")
        estado = input("informe o estado: ")
        x = time(id, nome, estado)
        cls.times.append(x)

    @classmethod
    def excluir_time(cls):
        UI.listar_time()
        id = int(input('informe o id do time a ser excluído: '))
        x = UI.listar_id(id)
        if x != None:
            #remove o contato atual
            cls.times.remove(x)
        
    @classmethod
    def inserir_jogador(cls):
        id = int(input("informe o id do jogador: "))
        nome = input("informe o nome: ")
        camisa = int(input("informe a camisa do jogador: "))
        idtime = int(input("informe o id do time do jogador: "))
        x = (id, nome, idtime, camisa)
        cls.jogadores.append(x)
        print("Jogador inserido com sucesso")
    
    @classmethod
    def listar_jogador(cls):
        if len(cls.jogadores) == 0: print("Nenhum jogador listado")
        else:
            for x in cls.jogadores: print(x)

    @classmethod
    def listar_id(cls, id):
        #procurar um item com o id informado
        for x in cls.jogadores:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar_jogador(cls):
        UI.listar_jogador()
        id = int(input('informe o id do time a ser alterado'))
        x = UI.listar_id(id)
        if x != None:
            #remove o contato atual
            cls.times.remove(x)
            #insere um novo contato com os dados atualizados
        nome = input("informe o nome: ")
        camisa = int(input("informe a camisa: "))
        idtime = int(input("informe o id do time: "))
        x = time(id, nome, camisa, idtime)
        cls.jogadores.append(x)

    @classmethod
    def excluir_jogador(cls):
        UI.listar_jogador()
        id = int(input('informe o id do jogador a ser excluído: '))
        x = UI.listar_id(id)
        if x != None:
            #remove o contato atual
            cls.jogadores.remove(x)
    @classmethod
    def listar_jogador_do_time(cls):
        id_time = int(input("informe o id do time: "))
        encontrou = False
        for j in cls.jogadores:
            if j.get_idtime() == id_time:
                print(j)
                encontrou = True 
        if not encontrou:
            print("Nenhum jogador encontrado nesse time")

    @classmethod
    def transferir_jogador(cls):
        id_jogador = int(input("Informe o ID do jogador: "))
        for j in cls.jogadores:
            if j.get_id() == id_jogador:
                novo_time = int(input("Informe o novo ID do time: "))
                # verifica se o time existe
                time_existe = False
                for t in cls.times:
                    if t.get_id() == novo_time:
                        time_existe = True
                        break
                    if time_existe:
                        j.set_idTime(novo_time)
                        print("Jogador transferido com sucesso!")
                    else:
                        print("Time não encontrado.")
                    return
            print("Jogador não encontrado.")


UI.main()