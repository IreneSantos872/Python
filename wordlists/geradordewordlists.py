import itertools

# resultado = itertools.permutations('abcdef', 3)
#
# for i in resultado:
#     print(''.join(i))

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))