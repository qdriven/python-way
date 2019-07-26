# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     split_user
   Description :
   Author :        patrick
   date：          2019/7/16
-------------------------------------------------
   Change Activity:
                   2019/7/16:
-------------------------------------------------
"""
__author__ = 'patrick'


count = 0
with open('all-users-ont-1.csv', 'r') as users:
    users = users.readlines()
    lists = []
    for user in users:
        if count <= 30000:
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