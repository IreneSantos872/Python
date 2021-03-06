import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

## ripem160 é algoritmo de hash de 160 bits
hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

## digest é o resumo do update
if hash1.digest() != hash2.digest():
    print(f'O arquivo:  {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.digest())
    print('O hash do arquivo b.txt é: ', hash2.digest())
else:
    print(f'O arquivo: {arquivo1} é igual o arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.digest())
    print('O hash do arquivo b.txt é: ', hash2.digest())
