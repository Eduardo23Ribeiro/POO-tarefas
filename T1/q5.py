class dados_pais:
    def __init__(self, nome, pop, km):
        self.nome = nome
        self.pop = pop
        self.km = km

    def calculo(self):
        densidade_demo = self.pop / self.km
        print(f"densidade demográfica do {self.nome} é de {densidade_demo:.2f} hab/km2")
        
d = dados_pais(str(input("digite o nome do país: ")), int(input("digite o a população do país: ")), int(input("digite a área em km ao quadrado do país: ")))
d.calculo()