#Importa o modulo ou biblioteca os(Integra os programas e recursos do S.O.
import os

print("#" * 60)   ##Imprimindo # 60 vezes

#criamos uma variável que vai receber do usuario um ip
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")


print("-" * 60)    ##Imprimindo - 60 vezes

##Chamando system da biblioteca os - comando ping -n -numeros de pacotes que serão 6{}
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 60)