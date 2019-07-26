# -*- coding:utf-8 -*-
import MySQLdb

# conn = MySQLdb.connect(host="10.213.128.98", port=13306
#                        , user="idc_exchange", password="123456"
#                        , db="idc_exchange")
conn = MySQLdb.connect(host="10.199.212.80", port=3306
                       , user="root", password="12345678"
                       , db="urcp")
print(conn)
conn.autocommit(on=True)
c = conn.cursor()

sql_blackfp = """
    insert into BlackFp(fp_device_id) VALUES ({fp_device_id})
"""
sql_blackTel = """
    insert into BlackTel(telephone) VALUES ({phone_no})
"""

from_count = 17000000000
for i in range(1, 10000):
    phoneno = from_count + i
    print(str(phoneno))
    c.execute(sql_blackTel.format(phone_no=phoneno))

# for i in range(1,100000):
#     print("99"+str(i))
#     c.execute()

c.close()
