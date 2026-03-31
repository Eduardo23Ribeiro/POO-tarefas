class conta_agua:
    def __init__(self,mes,ano,consumo):
        self.mes_x = mes
        self.ano_x = ano
        self.consumo = consumo
    def agua2(self):
        
        if self.consumo <= 10:
            preco = 38
           
        elif 11 <= self.consumo <= 20:
            preco = 38 + (self.consumo - 10) * 5
        elif self.consumo >= 21:
            preco = 83 + (self.consumo - 20) * 6

        print(f"O Mês é {self.mes_x} do ano {self.ano_x} e o preço foi de {preco}")
        
        
m = conta_agua(str(input("digite o o mês: ")), int(input("digite o ano: ")), int(input("digite o consumo ")))
m.agua2()