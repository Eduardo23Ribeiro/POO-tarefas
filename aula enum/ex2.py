import enum
from datetime import datetime

class Pagamento(enum.Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor(valor)
        self.__data_pagto = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO

    def set_cod_barras(self, cod):
        if len(cod) != 10:
            raise ValueError()
        self.__cod_barras = cod

    def set_data_emissao(self, emissao):
        if emissao > datetime.now():
            raise ValueError()
        self.__data_emissao = emissao

    def set_data_vencimento(self, venc):
        if venc < datetime.now():
            raise ValueError()
        self.__data_vencimento = venc

    def set_valor(self, valor):
        if valor < 0:
            raise ValueError()
        self.__valor_boleto = valor

    def pagar(self, valor_pago):
        if valor_pago < 0:
            raise ValueError()
        if self.__situacao_pagamento != Pagamento.EM_ABERTO:
            raise ValueError()
        self.__valor_pago = valor_pago
        self.__data_pagto = datetime.now()
        if self.__valor_boleto == self.__valor_pago:
            self.__situacao_pagamento = Pagamento.PAGO
        else:
            self.__situacao_pagamento = Pagamento.PAGO_PARCIAL

    def get_situacao_pagamento(self):
        return self.__situacao_pagamento

    def get_valor_boleto(self):
        return self.__valor_boleto

    def get_valor_pago(self):
        return self.__valor_pago

    def get_data_pagto(self):
        return self.__data_pagto

    def get_data_emissao(self):
        return self.__data_emissao

    def get_vencimento(self):
        return self.__data_vencimento

    def get_cod_barras(self):
        return self.__cod_barras

    def situacao_pagamento(self):
        return self.__situacao_pagamento

    def __str__(self):
        s = f"Boleto: {self.__cod_barras}"
        s += f"Valor: R${self.__valor_boleto:.2f} - Valor pago: R${self.__valor_pago:.2f}"
        s += f"Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')} - Valor: R${self.__valor_pago:.2f}"
        s += f"Data de pagamento: {self.__data_pagto}"
        return s

class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = BoletoUI.menu()
            if op == 1:
                BoletoUI.inserir()
            elif op == 2:
                BoletoUI.listar()
            elif op == 3:
                BoletoUI.vencidos()
            elif op == 4:
                BoletoUI.excluir()
            elif op == 5:
                BoletoUI.boletos_em_aberto()
            elif op == 6:
                BoletoUI.boletos_pagos()

    @staticmethod
    def menu():
        print("---------------------------------------")
        print("1 - Inserir, 2 - Listar, 3-Atualizar, 4 - Excluir")
        print("5 - Boletos em aberto, 6 - Boletos Pagos")
        print("7 - boletos a Vencer, 8 - boletos vencidos")
        print("9 - Total em aberto, 10 - Sair")
        print("---------------------------------------")
        return int(input("Digite a opção: "))

    @staticmethod
    def inserir():
        cod = input("Digite o código de barras: ")
        emissao = datetime.strptime(input("Digite a data de emissão (dd/mm/yyyy): "), "%d/%m/%Y")
        venc = datetime.strptime(input("Digite a data de vencimento (dd/mm/yyyy): "), "%d/%m/%Y")
        valor = float(input("Digite o valor do boleto: "))
        boleto = Boleto(cod, emissao, venc, valor)
        BoletoUI.__boletos.append(boleto)

    @staticmethod
    def listar():
        for boleto in BoletoUI.__boletos:
            print(boleto)

    @staticmethod
    def vencidos():
        for x in BoletoUI.__boletos:
            if x.get_situacao_pagamento() == Pagamento.EM_ABERTO and \
               x.get_vencimento() < datetime.now():
                print(x)

    @staticmethod
    def excluir():
        cod = input("Digite o código de barras do boleto a ser excluído: ")
        for boleto in BoletoUI.__boletos:
            if boleto.get_cod_barras() == cod:
                BoletoUI.__boletos.remove(boleto)
                print("Boleto excluído com sucesso!")
                return
        print("Boleto não encontrado.")

BoletoUI.main()