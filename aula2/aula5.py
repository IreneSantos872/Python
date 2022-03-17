lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'galinha', 'arara']
lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla[2])

#qtde de elementos na tupla
print(len(tupla))
print(len(lista_animal))

#converter a lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)


### Exercicio de Lista
# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante', 'galinha', 'arara']
# nova_lista = lista_animal
# print(nova_lista)
#
# # para adicionar um animal na lista
# lista_animal.append('lobo')
#
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
#
# lista_animal.reverse()
# print(lista_animal)
#
#
# # para retirar um item da lista com nro da posição
# lista_animal.pop(1)
#
# # para retirar um item da lista com nome
# lista_animal.remove('elefante')
# print(lista_animal[1])
#
# for x in lista_animal:
#     print(x)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista))
#
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um gato na lista')