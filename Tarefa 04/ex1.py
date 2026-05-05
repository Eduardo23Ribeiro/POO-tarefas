class Time:
    def __init__(self,id,nome,estadofederacao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estadofederacao(estadofederacao)
    def set_id(self, id):
        if id >= 0:
            self.id = id
        else:
            raise ValueError("ID inválido")        
    def set_nome(self, nome):
        if nome != "":
            self.nome = nome
        else:
            raise ValueError("Nome inválido")
    def set_estadofederacao(self,estadofederacao):
        if estadofederacao != "":
            self.estadofederacao = estadofederacao
        else:
            raise ValueError("Estado federativo inválido")
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_estadofederacao(self):
        return self.estadofederacao
    def __str__(self):
        return f"ID = {self.id} - Nome = {self.nome}"
class Jogador:
    def __init__(self,id,nome,camisa,idtime):
        self.set_id(id)
        self.set_nome(nome)
        self.set_camisa(camisa)
        self.set_idtime(idtime)
    def set_id(self, id):
        if id >= 0:
            self.id = id
        else:
            raise ValueError("ID inválido")
    def set_nome(self,nome):
        if nome != "":
            self.nome = nome
        else:
            raise ValueError("Nome inválido")
    def set_camisa(self,camisa):
        if camisa > 0:
            self.camisa = camisa
        else:
            raise ValueError("Número da camisa inválido")
    def set_idtime(self,idtime):
        if idtime >= 0:
            self.idtime = idtime
        else:
            raise ValueError("ID do time inválido")
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_camisa(self):
        return self.camisa
    def get_idioma(self):
        return self.idioma
    def __str__(self):
        return f"ID = {self.id} - Nome = {self.nome}"
class UI:
    time = []
    jogadores = []

    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1:
                UI.inserir_time()
            elif op == 2:
                UI.listar_time()
            elif op == 3:
                UI.atualizar_time()
            elif op == 4:
                UI.excluir_times()
            elif op == 5:
                UI.inserir_jogador()
            elif op == 6:
                UI.listar_jogador()
            elif op == 7:
                UI.atualizar_jogador()
            elif op == 8:
                UI.excluir_jogador()
            elif op == 9:
                UI.sair()
                print("Fim do programa")
            
          

    @staticmethod
    def menu():
        print("1-Inserir Time 2-Listar Times 3-Atualizar Time 4-Excluir Times 5-Inserir Jogador 6-Listar Jogadores 7-Atualizar Jogador 8-Excluir Jogador 9-Sair")
        return int(input("Escolha uma opção: "))    
    @classmethod
    def inserir_time(cls):
        id = int(input("Digite o ID do time: "))
        nome = int(input("Digite o nome do time: "))
        estadofederacao = int(input("Digite o estado da fedação do time "))
        y = Time(id,nome,estadofederacao)
        cls.time.append(y)
        print("Time inserido com sucesso!")
    @classmethod
    def listar_time(cls):
        for x in cls.time:
            print(x)
    @classmethod
    def atualizar_time(cls): 
        id = int(input("Digite o ID do time a ser atualizado: "))
        for x in cls.time:
            if x.get_id() == id:
                nome = int(input("Digite o novo nome do time: "))
                estadofederacao = int(input("Digite o novo estado da federação do time: "))
                x.set_nome(nome)
                x.set_estadofederacao(estadofederacao)
                print("Time atualizado com sucesso!")
                return
        print("Time não encontrado.")
    @classmethod
    def excluir_times(cls):
        id = int(input("Digite o ID do time a ser excluido: "))
        for x in cls.time:
            if x.get_id() == id:
                cls.time.remove(x)
                print("Time excluido com sucesso!")
                return
    def inserir_jogador(cls):
        id = int(input("Digite o ID do jogador: "))
        nome = int(input("Digite o nome do jogador: "))
        idtime = int(input("Digite o ID do time do jogador: "))
        camisa = int(input("Digite o número da camisa do jogador:"))
        y = Time(id,idtime,camisa)
        cls.time.append(y)
        print("Time inserido com sucesso!")
    def listar_jogador(cls):
        for x in cls.jogador:
            print(x)
    














UI.main()