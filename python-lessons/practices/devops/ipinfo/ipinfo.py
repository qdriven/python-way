# -*- coding: utf-8 -*-
# install IPy first

from IPy import IP

ip = IP('192.168.0.1/16')
print(ip.len())
for x in ip:
    print(x)

print([x in ip])

## reverseNames()
print(ip.reverseNames())
print(ip.iptype()) # private or public

print(ip.int())
print(ip.strHex())
print(ip.strBin())

## IP transferormation,IP mask

print(ip.make_net('255.255.255.0'))
print(IP('10.0.0.1/255.255.255.0',make_net=True))
print(IP('10.0.0.1/255.255.255.0').strNormal(0))
print(IP('10.0.0.1/255.255.255.0').strNormal(1))
print(IP('10.0.0.1/255.255.255.0').strNormal(2))
print(IP('10.0.0.1/255.255.255.0').strNormal(3))

#prefixlen,watprefixlen,overlaps


