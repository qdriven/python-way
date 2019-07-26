# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     mysql_records_demo
   Description :
   Author :        patrick
   date：          2019/7/15
-------------------------------------------------
   Change Activity:
                   2019/7/15:
-------------------------------------------------
"""
import pymysql

__author__ = 'patrick'

import records

pymysql.install_as_MySQLdb()

db = records.Database('mysql://root:ZA1Wt2trKA69SJq87DDr@13.229.242.153:3306/candybox')

sql = """
select Mobile from user
where IsCertification = 1 and InvitedONTID is not null
and length(Mobile)=11
order by 1 desc
"""

insert_sql = """
insert into candy_userproject (projectid, ontid,
                          GetDate, totalamount,
                          status,WithdrawAmount,ReceivedAmount)
                          values (46,"%s",unix_timestamp(),10,3,0,0);
"""

count = 0
with open('all-users-ont-1.csv', 'r') as users:
    users = users.readlines()
    lists = []
    for user in users:
        if count <= 2000:
            user_arr = user.split(",")
            insert_sql_real = insert_sql % user_arr[1].strip()
            print(insert_sql_real)
            lists.append(insert_sql_real)
            db.query(insert_sql_real)# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     mysql_records_demo
   Description :
   Author :        patrick
   date：          2019/7/15
-------------------------------------------------
   Change Activity:
                   2019/7/15:
-------------------------------------------------
"""
import pymysql

__author__ = 'patrick'

import records

pymysql.install_as_MySQLdb()

# db = records.Database('mysql://root:ZA1Wt2trKA69SJq87DDr@13.229.242.153:3306/candybox')

sql = """
select Mobile from user
where IsCertification = 1 and InvitedONTID is not null
and length(Mobile)=11
order by 1 desc
"""

insert_sql = """
insert into candy_userproject (projectid, ontid,
                          GetDate, totalamount,
                          status,WithdrawAmount,ReceivedAmount)
                          values (46,"%s",unix_timestamp(),10,3,0,0);
"""

count = 0
with open('all-users-ont-1.csv', 'r') as users:
    users = users.readlines()
    lists = []
    for user in users:
        if count <= 2000:
            # user_arr = user.split(",")
            # insert_sql_real = insert_sql % user_arr[1].strip()
            # print(insert_sql_real)
            lists.append(user)
            # db.query(insert_sql_real)
            count += 1
            print(count)
        else:
            break

with open('insert-'+str(count)+'.txt','w') as inserts:
    inserts.writelines(lists)
# rows = db.query(sql)
# print(rows)


# with open('insert-all.txt','w') as inserts:
#     inserts.writelines(lists)
# rows = db.query(sql)
# print(rows)
