import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
cursor = db.cursor()

cursor.execute("SELECT * FROM product")
result = cursor.fetchall()
print(result)
