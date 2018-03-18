from abc import ABC, abstractclassmethod


class TemplateCalculaImpostosMaximoMinimo(ABC):

    def calcula(self, orcamento):
        if self.condicao_maxima(orcamento):
            return self.calcula_condicao_maxima(orcamento)
        return self.calcula_condicao_minima(orcamento)

    @abstractclassmethod
    def condicao_maxima(self, orcamento):
        pass

    @abstractclassmethod
    def calcula_condicao_maxima(self, orcamento):
        pass

    @abstractclassmethod
    def calcula_condicao_minima(self, orcamento):
        pass


class ISS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICMP(TemplateCalculaImpostosMaximoMinimo):

    def condicao_maxima(self, orcamento):
        return orcamento.valor > 500

    def calcula_condicao_maxima(self, orcamento):
        return orcamento.valor * 0.1

    def calcula_condicao_minima(self, orcamento):
        return orcamento.valor * 0.08


class IJM(TemplateCalculaImpostosMaximoMinimo):

    def condicao_maxima(self, orcamento):
        return orcamento.valor > 500 and self.tem_item_que_vale_cem(orcamento)

    def calcula_condicao_maxima(self, orcamento):
        return orcamento.valor * 0.05

    def calcula_condicao_minima(self, orcamento):
        return orcamento.valor * 0.03

    def tem_item_que_vale_cem(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor >= 100:
                return True
        return False

