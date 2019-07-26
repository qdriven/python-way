# -*- coding: utf-8 -*-

# need to install dnspython first

# pip install dnspython

"""
.A hostname->ip address
.MX mailexchanger, mail server adress
.CNAME alias name for network, domain name mapping
.NS domain naming server and child servers
.PTR reverserNames, ip->host name
.SOA
rdclass
tcp
source
source_port
raise_on_no_answer
"""

import dns.resolver

## for domain name
A = dns.resolver.query("http://www.baidu.com", 'A')
for response in A.response.answer:
    for item in response.iterms:
        print(item.address)

## for MX
mx = dns.resolver.query("http://www.baidu.com", 'MX')
for item in mx:
    print(mx.preference, item.exchange)

## for NS
ns = dns.resolver.query("http://www.baidu.com", 'NS')
for item in ns:
    print(ns.to_text())

## for CNAME
cname = dns.resolver.query("http://www.baidu.com", 'CNAM')
for item in cname:
    print(ns.to_text())

# domain -> multiple ips
domain_name = "www.baidu.com"
ip_list = []


def get_ip_list(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print("dns resolver is failed for domain name %s" % domain)
        return
    for response in A.response.answer:
        for item in response.items:
            ip_list.add(item.address)
    return True;


def check_ip(ip, port="8080"):
    check_url = ip + port
    get_content = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(check_url)
    try:
        conn.request("GET", "/", headers={
            "Host": domain_name
        })
        r = conn.getresponse()
        get_content = r.read(15)
    finally:
        # realease the connection
        if get_content == "<! doctype html>":
            print(ip, " [PING OK]")
        else:
            print(ip, "[ PING EOOR]")


def check_domain_ips():
    if get_ip_list(domain_name) and len(ip_list) > 0:
        for ip in ip_list:
            check_ip(ip)
    else:
        print("dns resolver error.")

# putting there codes in crontab, making it running
        # in a certain time period manner
