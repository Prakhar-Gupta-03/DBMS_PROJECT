import mysql.connector
from mysql.connector import errorcode
#connecting to the database
db = mysql.connector.connect(host="localhost", user="prakhar", passwd="prakhar", database="test")
cursor = db.cursor()
#executing 10 queries 
#query 1
cursor.execute("SELECT category_ID,product_ID,product_name FROM Product WHERE Category_ID = 91 or Category_ID=34")
res = cursor.fetchall()
print(res)
#query 2
cursor.execute("Update admin_shop set admin_name='Rahul' where admin_id=1")
cursor.execute("SELECT ADMIN_NAME FROM ADMIN_SHOP WHERE ADMIN_ID = 1")
res = cursor.fetchall()
print(res)
#query 3
cursor.execute("UPDATE ADMIN_SHOP SET ADMIN_NAME = 'Anjali' WHERE ADMIN_ID = 1")
cursor.execute("SELECT ADMIN_NAME FROM ADMIN_SHOP WHERE ADMIN_ID = 1")
res = cursor.fetchall()
print(res)
#query 4
cursor.execute("SELECT AVG(order_amount) FROM ORDERS")
res = cursor.fetchall()
print(res)
cursor.execute("SELECT * FROM DELIVERY_MAN")    
res = cursor.fetchall()
print(res)
#query 5
cursor.execute("SELECT ORDER_ID FROM ORDERS WHERE ORDER_AMOUNT > 600")
res = cursor.fetchall()
print(res)
cursor.execute("SELECT COUNT(ORDER_ID) FROM ORDERS WHERE ORDER_AMOUNT > 600")
res = cursor.fetchall()
print(res)
#query 6
cursor.execute("Select * from product where category_ID in (Select category_ID from category where category_name='eggs' or category_name='milk')")
res = cursor.fetchall()
print(res)
#query 7
cursor.execute("SELECT CART_ID FROM CART WHERE EXISTS (SELECT CART_ID FROM CART WHERE PRODUCT_PRICE >1000 )")
res = cursor.fetchall()
print(res)
#query 8
cursor.execute("ALTER TABLE CUSTOMER ADD UNIQUE (CUSTOMER_ID)")
cursor.execute("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = 1")
res = cursor.fetchall()
print(res)
#query 9
cursor.execute("SELECT CATEGORY.CATEGORY_ID, CATEGORY.CATEGORY_NAME, PRODUCT.PRODUCT_ID, PRODUCT.PRODUCT_NAME FROM CATEGORY INNER JOIN PRODUCT ON CATEGORY.CATEGORY_ID = PRODUCT.CATEGORY_ID ORDER BY CATEGORY.CATEGORY_ID")
res = cursor.fetchall()
print(res)
#query 10
cursor.execute("SELECT CATEGORY_ID, COUNT(PRODUCT_ID) FROM PRODUCT GROUP BY CATEGORY_ID")
res = cursor.fetchall()
print(res)
#query 11
cursor.execute("SELECT DELIVERY_MAN.delivery_man_id, DELIVERY_MAN.man_name, ORDERS.ORDER_ID, ORDERS.order_amount, CUSTOMER.CUSTOMER_FNAME,  CUSTOMER.Customer_Address_BuildingNo, CUSTOMER.Customer_Address_Street, CUSTOMER.Customer_Address_City, CUSTOMER.Customer_Address_State, Customer_Address_Pincode  FROM ORDERS INNER JOIN DELIVERY_MAN ON ORDERS.ORDER_ID = DELIVERY_MAN.ORDER_ID INNER JOIN CUSTOMER ON ORDERS.CUSTOMER_ID = CUSTOMER.CUSTOMER_ID")
res = cursor.fetchall()
print(res)
