import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="project",
    passwd="project",
    database="mydatabase"

)
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(35), LastName VARCHAR(15), Address VARCHAR(35))"
    )# COMMAND TO CREATE A TABLE