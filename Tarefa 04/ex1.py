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
        return f"ID = {self.id} - Nome = {self.nome} - Estado federativo = {self.estadofederacao}"
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