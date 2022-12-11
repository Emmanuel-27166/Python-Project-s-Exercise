import mysql.connector

from ModuleForDB import mydb,mycursor

# here we insert values
sql = "INSERT INTO customers ( Name, LastName, Address) VALUES (%s, %s, %s)"

val = [
    ("Sorie", 'Bangura', '22 Quary Freetown'),
    ("Alie", 'Bangura', '25 Quary Freetown'),
    ("Mohamed", 'Bangura', '24 Quary Freetown'),
    ("Abie", 'Bangura', '223 Quary Freetown'),
    ("Emmanuel", 'Bangura', '212 Quary Freetown'),
    ("Brime", 'Bangura', '22 Quary Freetown'),
    ("Sorie7", 'Bangura', '22 Quary Freetown'),
    ("Sorie6", 'Bangura', '22 Quary Freetown'),
    ("Sorie5", 'Bangura', '22 Quary Freetown'),
    ("Sorie4", 'Bangura', '22 Quary Freetown'),
    ("Sorie3", 'Bangura', '22 Quary Freetown'),
    ("Sorie2", 'Bangura', '22 Quary Freetown'),
    ("Sorie1", 'Bangura', '22 Quary Freetown'),
    ("Sorie10", 'Bangura', '22 Quary Freetown')
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "Data inserted Successfully into Customer Database.")