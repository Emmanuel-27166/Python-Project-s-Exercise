import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="project",
    passwd="project",
    database="mydatabase"

)
mycursor = mydb.cursor()