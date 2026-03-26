class maior:
    q

    def calc(self):
        if self.op_str == "/":
            return self.valor_a / self.valor_b
        elif self.op_str == "*":
            return self.valor_a * self.valor_b
        elif self.op_str == "+":
            return self.valor_a + self.valor_b
        elif self.op_str == "-":
            return self.valor_a - self.valor_b
        else:
            return "Digite uma operação listada acima"

m = maior(int(input("valor 1: ")), int(input("valor 2: ")), str(input("digite + ou - ou * ou /: ")))  
print(m.calc())