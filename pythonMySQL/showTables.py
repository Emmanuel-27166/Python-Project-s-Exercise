import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="project",
    passwd="project",
    database="mydatabase"

)
mycursor = mydb.cursor()
mycursor.execute("show Tables")# the command to show a table
for x in mycursor:
    print(x)