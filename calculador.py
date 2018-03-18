from descontos import  DescontoMaisDeCincoItens, DescontoMaisDeQuinhentosReais, SemDesconto

class CalculadorDeImpostos(object):

    def realiza_calculo(self, orcamento, imposto):

        imposto = imposto.calcula(orcamento)
        print(imposto)

class CalculadorDeDescontos(object):

    def realiza_calculo(self, orcamento):

        desconto = DescontoMaisDeCincoItens(
            DescontoMaisDeQuinhentosReais(
                SemDesconto()
            )
        ).calcula(orcamento)

        print(desconto)

