class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return { "id": self.idade, "nome": self.nome }
    def to_json(self):
        return { "id": self.idade, "nome": self.nome }
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"])
    
a = Cliente(1,"Jon kook")
b = Cliente(2,"Jimin kim jon um")
c = Cliente.from_json({"id": 3, "nome": "Kim taehyung"})

print(a)
print(b)
print(c)
print(a.__dict__)
print(b.__dict__)
print(vars(a))
print(vars(b))
