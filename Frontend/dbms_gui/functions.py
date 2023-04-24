from datetime import time, datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QTableView, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QLabel, \
    QLineEdit, QVBoxLayout, QWidget
import mysql.connector
# connect to database



def exit_application(self):
    QApplication.quit()
def view_products(self):
    widget = QWidget(self)
    layout = QVBoxLayout(widget)
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product")
    res = cursor.fetchall()
    self.table = QTableWidget()
    # self.setCentralWidget(self.table)

    self.table.setRowCount(len(res))
    self.table.setColumnCount(6)
    self.table.setHorizontalHeaderLabels(["Product_ID", "Product_name", "Product_price", "Product_quantity", "Category_ID", "Admin_ID"])
    print(len(res))
    print(res)
    for i in range(0, len(res)):
        for j in range(0, 6):
            print(res[i][j])
            self.table.setItem(i,j,QTableWidgetItem(str(res[i][j])))

    self.back_button = QPushButton("Back")
    # place the button at such coordinates that it is visible
    # self.back_button.move(500, 50)
    # self.back_button.clicked.connect(self.customer_menu)

    layout.addWidget(self.table)
    layout.addWidget(self.back_button)
    layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
    self.setCentralWidget(widget)

    return self
# def go_back(self):
# #     show customer menu
#     self.customer_menu()
# def view_products(self):
#     layout = QVBoxLayout(self)
#     db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM product")
#     res = cursor.fetchall()
#     self.table = QTableWidget()
#     self.setCentralWidget(self.table)
#
#     self.table.setRowCount(len(res))
#     self.table.setColumnCount(6)
#     self.table.setHorizontalHeaderLabels(["Product_ID", "Product_name", "Product_price", "Product_quantity", "Category_ID", "Admin_ID"])
#     print(len(res))
#     print(res)
#     for i in range(0, len(res)):
#         for j in range(0, 6):
#             print(res[i][j])
#             self.table.setItem(i,j,QTableWidgetItem(res[i][j]))
#     return self.table
def view_categories(self):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM category")
    res = cursor.fetchall()
    self.table = QTableWidget()
    self.setCentralWidget(self.table)

    self.table.setRowCount(len(res))
    self.table.setColumnCount(3)
    self.table.setHorizontalHeaderLabels(["Admin_ID", "Category_ID", "Category_name"])

    print(len(res))
    print(res)
    for i in range(0, len(res)):
        for j in range(0,3):
            print(res[i][j])
            self.table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
    return self.table


def add_product_func(self,name,price,quantity,category):
    # print("in add product func")
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    Admin_ID = 1
    product_name = name
    product_price = price
    product_quantity = quantity
    Category_ID = category
    # product_name = input("Enter product name: ")
    # product_price = int(input("Enter product price: "))
    # product_quantity = int(input("Enter product quantity: "))
    # Category_ID = input("Enter product category: ")
    try:
        # print("till here")
        cursor.execute("insert into product (product_name, product_price, product_quantity, Category_ID, Admin_ID) values (%s, %s, %s, %s, %s)",
            (product_name, product_price, product_quantity, Category_ID, Admin_ID,))
        db.commit()
        # print("Product added successfully")
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))

def add_category_func(self,name):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    Admin_ID = 1
    category_name = name
    # category_name = input("Enter category name: ")
    try:
        cursor.execute("insert into category (category_name,Admin_ID) values (%s, %s)", (category_name, Admin_ID,))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))

def change_price_func(self,id,price):
    print("in change price func")
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    product_id = id
    product_price = price
    print(product_id)
    cursor.execute("select product_id from product where product_id = %s", (product_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Product does not exist")
    else:
        try:
            cursor.execute("update product set product_price = %s where product_id = %s", (product_price, product_id,))
            db.commit()
        except:
            print("Bruh wtf!!!")
            # QMessageBox.about(self, "Success", "Price changed successfully")
            # print("Error: {}".format(err.msg))


def change_quan_func(self,id,quantity):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    product_id = id
    product_quantity = quantity
    cursor.execute("select product_id from product where product_id = %s", (product_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Product does not exist")
    else:
        try:
            cursor.execute("update product set product_quantity = %s where product_id = %s", (product_quantity, product_id,))
            db.commit()
        except:
            print("Bruh wtf!!!")









def remove_product_func(self,product_id):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    product_id = product_id
    # check if product exists
    cursor.execute("select product_id from product where product_id = %s", (product_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Product does not exist")
    else:
        # remove the product from the cart
        cursor.execute("delete from cart where product_id = %s", (product_id,))
        cursor.execute("delete from all_orders where product_id = %s", (product_id,))
        cursor.execute("delete from product where product_id = %s", (product_id,))
        db.commit()
        print("Product removed successfully")

def remove_category_func(self):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    category_name = input("Enter category name: ")
    # check if category exists
    cursor.execute("select category_id from category where category_name = %s", (category_name,))
    res = cursor.fetchall()
    print(res)
    if len(res) == 0:
        print("Error: Category does not exist")
    else:
        # remove all the products in the category
        # cursor.execute("select product_id from product where Category_ID = %s", (res[0][0],))
        # res = cursor.fetchall()
        for i in res:
            print(i[0])
        #     # remove the products from the cart
        #     cursor.execute("delete from cart where product_id = %s", (i[0],))
        #     cursor.execute("delete from all_orders where product_id = %s", (i[0],))
        #     cursor.execute("delete from product where product_id = %s", (i[0],))
        # remove the category
            cursor.execute("delete from category where category_id = %s", (i[0],))
        #     db.commit()
        print("Category removed successfully")

def view_cart(self,customer_id):
    customer_id = customer_id
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    cursor.execute("select * from cart where customer_id = %s", (customer_id,))
    # print("1")
    res = cursor.fetchall()
    print(res)
    self.table = QTableWidget()
    # self.setCentralWidget(self.table)

    self.table.setRowCount(len(res))
    self.table.setColumnCount(5)
    self.table.setHorizontalHeaderLabels(["Product ID", "Product Quantity", "Product Price", "Category ID","Product_Name"])

    # # print(len(res))
    # # print(res)
    # for i in range(0, len(res)):
    #     for j in range(0, 4):
    #         print(res[i][j])
    #         self.table.setItem(i, j, QTableWidgetItem(res[i][j]))

    for i in range(len(res)):
        cursor.execute("select * from product where product_id = %s", (res[i][1],))
        product_name = cursor.fetchall()
        print(product_name)
        self.table.setItem(i, 0, QTableWidgetItem(str(res[i][1])))
        self.table.setItem(i, 1, QTableWidgetItem(str(res[i][2])))
        self.table.setItem(i, 2, QTableWidgetItem(str(product_name[0][2])))
        self.table.setItem(i, 3, QTableWidgetItem(str(product_name[0][4])))
        self.table.setItem(i, 4, QTableWidgetItem(str(product_name[0][1])))
    #     show the table
    # self.table.show()
    return self.table

def add_to_cart_func(self,id,quantity,customer_id):
    print("3")
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    id = id
    quantity = quantity
    customer_id = customer_id
    print("quantity", quantity)
    try:
        cursor.execute(
            "INSERT INTO CART(customer_id, product_id, product_quantity) VALUES (%s, %s, %s)",
            (customer_id, id, quantity))
        db.commit()
    except ValueError:
        print("Invalid input. Please try again.")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        text_error = err.msg
        if (text_error == "Product already exists in cart"):
            try:
                cursor.execute(
                    "UPDATE CART SET product_quantity = product_quantity + %s WHERE customer_id = %s AND product_id = %s",
                    (quantity, customer_id, id))
                db.commit()
            except mysql.connector.Error as err:
                print("Error: {}".format(err))


def place_order(self,customer_id):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    id = customer_id
    try:
        cursor.execute(
            "INSERT INTO ORDERS(customer_id, order_datetime) VALUES (%s, now())", (id,))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return
    else:
        try:
            # find the order_id of the order placed
            cursor.execute(
                "select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
            res = cursor.fetchall()
            order_id = res[0][0]
            # find the total price of the order placed
            cursor.execute(
                "select sum(product.product_price*cart.product_quantity) from product, cart where product.product_id = cart.product_id and cart.customer_id = %s",
                (id,))
            res = cursor.fetchall()
            total_price = res[0][0]
            # update the order_amount in the orders table
            cursor.execute(
                "update orders set order_amount = %s where order_id = %s", (total_price, order_id))
            db.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return
        else:
            print("Order placed successfully!")
    # time.sleep(2)
    print("Processing the order...")
    # adding all the products from the cart to the all_orders table along with the order_id
    cursor.execute(
        "select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
    res = cursor.fetchall()
    order_id = res[0][0]
    cursor.execute(
        "select product_id, product_quantity from cart where customer_id = %s", (id,))
    res = cursor.fetchall()
    for i in res:
        cursor.execute(
            "insert into all_orders(order_id, customer_id, product_id, product_quantity, product_price) values (%s, %s, %s, %s, (select product_price from product where product_id = %s))",
            (order_id, id, i[0], i[1], i[0]))
        db.commit()
    # print the order details
    print("----------------------------------BILL----------------------------------")
    print()
    print("Order ID: " + str(order_id))
    # print("Order date and time: " + str(datetime.datetime.now()))
    print("Product ID\tProduct quantity\tProduct price\t\tProduct Name")
    total_quantity = 0
    cursor.execute(
        "select product_id, product_quantity, product_price from all_orders where customer_id = %s and order_id = %s",
        (id, order_id))
    res = cursor.fetchall()
    for i in res:
        cursor.execute(
            "select product_name from product where product_id = %s", (i[0],))
        res1 = cursor.fetchall()
        print(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" +
              str(i[2]) + "\t\t\t" + str(res1[0][0]))
        total_quantity += i[1]
    print("Total price: " + str(total_price))
    print("Total quantity: " + str(total_quantity))
    print("------------------------------------------------------------------------")
    # updating the product quantity in the product table
    cursor.execute(
        "select product_id, product_quantity from cart where customer_id = %s", (id,))
    res = cursor.fetchall()
    for i in res:
        cursor.execute(
            "update product set product_quantity = product_quantity - %s where product_id = %s", (i[1], i[0]))
        db.commit()
    # removing all the products from the cart
    cursor.execute("DELETE FROM CART WHERE CUSTOMER_ID = %s", (id,))
    # pause execution of the program for 1 seconds
    print("Assigning a delivery man for the order...")
    # time.sleep(2)
    # try:
        # finding the delivery man with the least number of orders
        # getting a count of all the deliveries assigned for each delivery man
    cursor.execute(
        "Select delivery_man.delivery_man_id, count(order_delivery_man.order_ID) as number_of_deliveries from delivery_man left join order_delivery_man on delivery_man.delivery_man_id = order_delivery_man.delivery_man_id group by delivery_man.delivery_man_id order by number_of_deliveries ASC")
    res = cursor.fetchall()
    assigned_delivery_man_id = res[0][0]
    # finding the order_id of the order placed
    cursor.execute(
        "select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
    res = cursor.fetchall()
    order_id = res[0][0]
    # assigning the order with order_id to the delivery_man
    cursor.execute("insert into order_delivery_man(delivery_man_id, order_id, delivery_date) values(%s, %s, now())",
                   (assigned_delivery_man_id, order_id))
    db.commit()
    print("Order is assigned to a delivery man successfully!")
    # except mysql.connector.Error as err:
    #     print("Error: {}".format(err))
    #     return

def view_order(self,customer_id):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    id = customer_id
    # count the number of orders placed by the customer
    cursor.execute(
        "select count(*) from all_orders where customer_id = %s group by order_id", (id,))
    res = cursor.fetchall()
    print("Number of orders placed: " + str(len(res)))
    # display the order history
    cursor.execute(
        "select order_id from all_orders where customer_id = %s group by order_id", (id,))
    res = cursor.fetchall()
    for i in res:
        print()
        print("-------------------------------------------------------------------")
        print("Order ID: " + str(i[0]))
        cursor.execute(
            "select product_ID, product_quantity, product_price from all_orders where customer_id = %s and order_id = %s",
            (id, i[0]))
        res1 = cursor.fetchall()
        total_price = 0
        total_quantity = 0
        print("Product_ID\tProduct_quantity\tProduct_price\t\tProduct_Name")
        for j in res1:
            cursor.execute(
                "select product_name from product where product_id = %s", (j[0],))
            res2 = cursor.fetchall()
            print(str(j[0]) + "\t\t\t" + str(j[1]) + "\t\t\t" +
                  str(j[2]) + "\t\t\t" + str(res2[0][0]))
            total_price += j[1] * j[2]
            total_quantity += j[1]
        print()
        print("Total price: " + str(total_price))
        print("Total quantity: " + str(total_quantity))
        print("-------------------------------------------------------------------")

def add_money_to_wallet_func(id,amount):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    id = id
    amount = amount
    cursor.execute("update customer set customer_wallet=customer_wallet+" + amount + " where customer_id=" + str(id))
    db.commit()
