from datetime import datetime
from mailbox import NotEmptyError
from tkinter import Menu

class Paciente:
    def __init__(self, id, n, c, t, nasc):
        self.set_id(id)
        self.set_nome(n)
        self.set_cpf(c)
        self.set_telefone(t)
        self.set_nascimento(nasc)

    def set_id(self, v):
        if v < 0: raise ValueError()
        self.__id = v

    def set_nome(self, n):
        if n == "": raise ValueError()
        self.__nome = n

    def set_cpf(self, n): 
        if n == "": raise ValueError()
        self.__cpf = n

    def set_telefone(self, n): 
        if n == "": raise ValueError()
        self.__telefone = n

    def set_nascimento(self, n):    
        if n > datetime.now(): raise ValueError()
        self.__nascimento = n

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return f'O id: {self.__id}, Nome: {self.__nome}, CPF: {self.__cpf}, Telefone: {self.__telefone},\nNascimento {self.__nascimento.strftime("%d/%m/%y")}'

    def idade(self):
        idade = datetime.now() - self.__nascimento
        anos = idade.days // 365 
        meses = idade.days % 365 // 30
        return f'Idade: {anos}, Meses: {meses}'

class UI:
    __pacientes = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
            if op == 5: UI.pesquisar()
            if op == 6: UI.aniversariantes()

    @staticmethod
    def menu():
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("3 - Pesquisar")
        print("3 - Aniversariantes")
        print("9 - Fim")
        op = int(input("Informe uma opção: "))
        return op

    @classmethod
    def inserir(cls):  
        id = int(input('id: '))
        nome = (input('nome: '))
        cpf = (input('cpf: '))
        telefone = (input('telefone: '))
        nasc = datetime.strptime(input('nascimento: '), "%d%m%y" )

        x = Paciente(id, nome, cpf, telefone, nasc)

        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__pacientes: print(x, x.idade())
    @classmethod
    def atualizar(cls):
        for x in cls.__pacientes: print(x)
        id = int(input('Informe o id do paciente a ser atualizado: '))
        for x in cls.__pacientes:
            if x.get_id() == id:
                nome = (input('nome: '))
                cpf = (input('cpf: '))
                telefone = (input('telefone: '))
                nasc = datetime.strptime(input('nascimento: '), "%d%m%y" )
                x.set_nome(nome)
                x.set_cpf(cpf)
                x.set_telefone(telefone)
                x.set_nascimento(nasc)
                print("Paciente atualizado com sucesso!")
                
    @classmethod
    def excluir(cls):
        for x in cls.__pacientes: print(x)
        id = int(input('Informe o id do paciente a ser excluído: '))
        for x in cls.__pacientes:
            if x.get_id() == id:
                cls.__pacientes.remove(x)
                print("Paciente excluído com sucesso!")
        print("Paciente não encontrado!")
    @classmethod
    def pesquisar(cls):
        s = input("informe as inicias do nome: ")
        for x in cls.__pacientes:  
            if x.get_nome().starswith(s): print(x)
    @classmethod
    def aniversariantes(cls):
        m = int(input("informe o mes para a lista de aniversariantes (1-12)"))
        for x in cls.__pacientes:
            if x.get_nome().starswith(m): print(x)    
        
UI.main()