import mysql.connector
# from pythonMySQL import ModuleForDB 
from ModuleForDB import mydb, mycursor

# mycursor  =  mydb.cursor()
sql = "INSERT INTO customers(Name, LastName, Address) VALUES (%s,%s, %s)"
val = ("emmanuel", "Unique","22 Makakura")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted successfully")
