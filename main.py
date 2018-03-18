from calculador import CalculadorDeImpostos, CalculadorDeDescontos
from orcarmento import Orcamento, Item
from impostos import ISS, ICMS

orcamento = Orcamento()

orcamento.adiciona_item(Item('Item 1', 100))
orcamento.adiciona_item(Item('Item 2', 50))


calculadorDeImpostos = CalculadorDeImpostos()
calculadorDeDescontos = CalculadorDeDescontos()

calculadorDeImpostos.realiza_calculo(orcamento, ISS())
calculadorDeImpostos.realiza_calculo(orcamento, ICMS())

calculadorDeDescontos.realiza_calculo(orcamento)
