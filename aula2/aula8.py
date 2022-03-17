from aula7televisao import Televisao
from aula7 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['galinha', 'elefante', 'macaco']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da Lista: {}'.format(total_letras))

