import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="project",
    passwd="project",
    database="mydatabase"

)
mycursor = mydb.cursor()
mycursor.execute("show databases")# the command to show a database
for x in mycursor:
    print(x)