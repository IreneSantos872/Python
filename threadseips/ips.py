import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco + 100)

ip2 = '192.168.0.0/24'
rede = ipaddress.ip_network(ip2)
ip2 = '192.168.0.0/16'
rede2 = ipaddress.ip_network(ip2, strict=False)

print(rede)
print(rede2)

for ip2 in rede2:
    print(ip2)