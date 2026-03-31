class dados_pais:
    def __init__(self, nome, pop, km):
        self.nome = nome
        self.pop = pop
        self.km = km
        self.densidade = self.pop / self.km

    def mostrar(self):
        print(f"Densidade demográfica de {self.nome}: {self.densidade:.2f} hab/km²")

    
    def __lt__(self, outro):
        return self.densidade < outro.densidade


lista = []

for i in range(10):
    nome = input("Digite o nome do país: ")
    pop = int(input("Digite a população: "))
    km = int(input("Digite a área em km²: "))

    pais = dados_pais(nome, pop, km)
    pais.mostrar()
    lista.append(pais)


maior = max(lista)

print(f"\nPaís com maior densidade: {maior.nome} ({maior.densidade:.2f} hab/km²)")