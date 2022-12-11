import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="project",
    passwd="project",
    database="mydatabase"

)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")#command to create a database
