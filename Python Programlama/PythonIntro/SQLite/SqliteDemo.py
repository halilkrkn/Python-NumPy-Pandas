# -*- coding: utf-8 -*-

import sqlite3 as sqlite

connection = sqlite.connect("chinook.db")

#cursor = connection.execute("""select FirstName, LastName 
#                             from customers where city='Prague'""")
#
#for row in cursor:
#    print("first Name: " + row[0])
#    print("last Name: " + row[1])
#    print("*********")

cursor = connection.execute("""select city, count(*) from customers 
                            group by city order by city""")
for row in cursor:
    print("city = " +row[0])
    print("count = " +str(row[1]))
    print("*********")

connection.close()