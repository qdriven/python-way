# -*- coding: utf-8 -*-
# http://www.dnspython.org/examples.html

import dns.resolver

domain = "localhost:8080"

cname = dns.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print(j.to_text())

