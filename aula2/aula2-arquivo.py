a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b


print('Soma: {}. Subtração: {}'.format(soma, subtracao))
print('Soma: {soma}. \nSubtração: {sub}.\nMultiplicao: {multiplicacao}.'
      ' \nDivisao: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                sub=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))
