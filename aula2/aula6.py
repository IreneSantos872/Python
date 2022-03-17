# # manipular conjunto
#
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
# conjunto_uniao = conjunto1.union(conjunto2)
# print(type(conjunto_uniao))
#

### para adicionar
conjunto1.add(9)

### para excluir
conjunto1.discard(2)
print(conjunto1)


# conjunto_interseccao = conjunto1.intersection(conjunto2)
# print(conjunto_interseccao )
#
# conjunto_diferencial = conjunto1.difference(conjunto2)
# conjunto_diferencial2 = conjunto2.difference(conjunto1)
# print('Diferença entre 1 e 2: {}'.format(conjunto_diferencial)
# #print('Diferença entre 2 e 1: {}'.format(conjunto_diferencial2)
#
# #conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
# #print('Diferença Simetrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_b.issubset(conjunto_a)
conjunto_superset = conjunto_b.issubset(conjunto_a)
print('A é subconjunto de B: {}'.format(conjunto_subset))
print('B é subconjunto de A: {}'.format(conjunto_superset))

## conversão de lista para conjunto

lista = ['cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)

## conversão de conjunto para lista
lista_animais = list(conjunto_animais)
print(lista_animais)


