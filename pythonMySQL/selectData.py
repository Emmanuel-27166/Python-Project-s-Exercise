import mysql.connector

from ModuleForDB import mydb,mycursor

print()
mycursor.execute("select * from customers")
myResult  = mycursor.fetchall()

for x in myResult:
    print(x)