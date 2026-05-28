import enum
from datetime import datetime

class Pagamento(enum.Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod,emissao, venc,valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor(valor)
        self.__data_pagto = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO

    def set_cod_barras(self,cod):
        if len(cod) != 10: raise ValueError()
        self.__cod_barras = cod
    x = 25
    y = 0 if x < 10 else 15
    def set_data_emissao(self,emissao):
        if emissao > datetime.now(): raise ValueError()
        self.__data_emissao = emissao
    def set_data_vencimento(self,venc):
        if venc < datetime.now: raise ValueError()
        self.__data_vencimento = venc
    def set_valor(self,valor):
        if valor < 0: raise ValueError()
        self.__valor_boleto = valor
    def pagar(self,valor_pago):
        if valor_pago < 0: raise ValueError()
        if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError()
        self.__valor_pago = valor_pago
        self.__data_pagto = datetime.now()
        if self.__valor_boleto == self.__valor_pago: self.__situacao_pagamento = Pagamento.PAGO
        else: self.__situacao_pagamento = Pagamento.PAGO_PARCIAL
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
        s += f"Vencimento: {self.__data_vencimento.strftime("%d/%m/%Y")} - Valor: R${self.__valor_pago:.2f}"
        s += f"Data de pagamento: {self.__data_pagto}"
        return s