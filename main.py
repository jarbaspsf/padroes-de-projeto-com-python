from calculador import CalculadorDeImpostos, CalculadorDeDescontos
from orcarmento import Orcamento, Item
from impostos import ISS, ICMS, ICMP, IJM

orcamento = Orcamento()

orcamento.adiciona_item(Item('Item 1', 100))
orcamento.adiciona_item(Item('Item 2', 500))


calculadorDeImpostos = CalculadorDeImpostos()
calculadorDeDescontos = CalculadorDeDescontos()

print("ICM")
calculadorDeImpostos.realiza_calculo(orcamento, ISS())
print("ICMS")
calculadorDeImpostos.realiza_calculo(orcamento, ICMS())

print("ICMP")
calculadorDeImpostos.realiza_calculo(orcamento, ICMP())
print("IJM")
calculadorDeImpostos.realiza_calculo(orcamento, IJM())

