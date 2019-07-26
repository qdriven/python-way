# -*- coding: utf-8 -*-
from IPy import IP

ips = IP('127.0.0.1')

if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse address: %s' % ips.reverseNames()[0])

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())
