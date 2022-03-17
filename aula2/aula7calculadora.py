class Calculadora:
    def __init__(self):
        pass


    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a, valor_b ):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return  valor_a *  valor_b

    def divisao(self, valor_a, valor_b):
        return  valor_a /  valor_b


    calculadora = Calculadora()
    print(calculadora.soma(5, 6))
    print(calculadora.subtracao(20, 8))
    print(calculadora.multiplicacao(5, 3))
    print(calculadora.divisao(40, 5))
